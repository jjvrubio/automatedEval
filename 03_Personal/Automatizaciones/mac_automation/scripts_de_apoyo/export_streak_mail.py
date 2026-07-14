#!/usr/bin/env python3
"""
Export Mail.app messages from notifications@streak.com to JSON
Accesses Mail.app SQLite database directly for better performance
"""

import sqlite3
import json
import os
from pathlib import Path
from datetime import datetime
import re

# Configuración
STREAK_SENDER = "notifications@streak.com"
TARGET_MAILBOX = "potenciales"  # Cambiar a "Embudo" o el nombre que necesites


def find_mail_database():
    """Encuentra la base de datos de Mail.app"""
    mail_v10 = Path.home() / "Library" / "Mail" / "V10" / "MailData" / "Envelope Index"
    mail_v9 = Path.home() / "Library" / "Mail" / "V9" / "MailData" / "Envelope Index"
    mail_v8 = Path.home() / "Library" / "Mail" / "V8" / "MailData" / "Envelope Index"
    
    for db_path in [mail_v10, mail_v9, mail_v8]:
        if db_path.exists():
            return db_path
    
    raise FileNotFoundError("No se encontró la base de datos de Mail.app")


def clean_text(text):
    """Limpia el texto eliminando caracteres de control"""
    if not text:
        return ""
    # Convertir a string si es necesario
    if not isinstance(text, str):
        text = str(text)
    # Eliminar caracteres de control excepto tabs y newlines
    text = re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F\x7F]', '', text)
    return text.strip()


def extract_plain_text(content):
    """Extrae texto plano de contenido HTML o texto"""
    if not content:
        return ""
    
    # Si es HTML, intentar extraer texto básico
    if '<html' in content.lower() or '<body' in content.lower():
        # Eliminar tags HTML básicos
        text = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text)
        return clean_text(text)
    
    return clean_text(content)


def export_streak_emails():
    """Exporta correos de Streak desde Mail.app"""
    db_path = find_mail_database()
    print(f"📧 Conectando a base de datos: {db_path}")
    
    # Conectar a la base de datos (solo lectura)
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        # Buscar mensajes de Streak en la carpeta Embudo de la cuenta pleasepoint
        # Primero explorar la estructura para encontrar las columnas correctas
        print("\n🔍 Inspeccionando estructura de la base de datos...")
        
        # Obtener columnas de la tabla messages
        cursor.execute("PRAGMA table_info(messages)")
        columns = [row[1] for row in cursor.fetchall()]
        print(f"   Columnas disponibles en 'messages': {', '.join(columns[:10])}...")
        
        # Buscar TODOS los mailboxes que contengan el nombre objetivo
        cursor.execute("""
            SELECT ROWID, url
            FROM mailboxes 
            WHERE url LIKE ?
        """, (f'%{TARGET_MAILBOX}%',))
        all_target_mailboxes = cursor.fetchall()
        
        if not all_target_mailboxes:
            raise ValueError(f"No se encontró ningún mailbox con '{TARGET_MAILBOX}'")
        
        mailbox_ids = [mb[0] for mb in all_target_mailboxes]
        print(f"✓ Encontrados {len(mailbox_ids)} mailboxes con '{TARGET_MAILBOX}':")
        for mb in all_target_mailboxes:
            print(f"  - ID {mb[0]}: {mb[1]}")
        
        # Query optimizada para V10 - buscar en TODOS los mailboxes de Embudo
        placeholders = ','.join('?' * len(mailbox_ids))
        query = f"""
        SELECT DISTINCT
            m.subject,
            m.ROWID as message_id,
            m.date_received,
            addr.address AS sender_email,
            addr.comment AS sender_name
        FROM messages m
        LEFT JOIN addresses addr ON m.sender = addr.ROWID
        WHERE addr.address = ?
        AND m.mailbox IN ({placeholders})
        ORDER BY m.date_received DESC
        """
        
        cursor.execute(query, (STREAK_SENDER, *mailbox_ids))
        messages = cursor.fetchall()
        
        print(f"✓ Encontrados {len(messages)} mensajes de {STREAK_SENDER} en '{TARGET_MAILBOX}'")
        
        # Convertir a formato JSON
        results = []
        for msg in messages:
            results.append({
                "subject": clean_text(msg['subject']),
                "content": "(pendiente de extraer del archivo .emlx)",
                "date_received": msg['date_received'],
                "sender": f"{msg['sender_name'] or ''} <{msg['sender_email'] or ''}>".strip(),
                "message_id": msg['message_id']
            })
        
        # Guardar a JSON
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = Path(__file__).parent / f"Streak-mails-{timestamp}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Exportados {len(results)} correos a: {output_file}")
        return output_file
        
    finally:
        conn.close()


def export_with_full_content():
    """
    Versión alternativa que intenta extraer el contenido completo
    Nota: Mail.app guarda los correos en archivos .emlx individuales
    """
    db_path = find_mail_database()
    mail_dir = db_path.parent.parent
    
    print(f"📧 Conectando a base de datos: {db_path}")
    print(f"📁 Directorio de Mail: {mail_dir}")
    
    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        
        # Buscar TODOS los mailboxes que contengan el nombre objetivo
        cursor.execute("""
            SELECT ROWID, url
            FROM mailboxes 
            WHERE url LIKE ?
        """, (f'%{TARGET_MAILBOX}%',))
        all_target_mailboxes = cursor.fetchall()
        
        if not all_target_mailboxes:
            raise ValueError(f"No se encontró ningún mailbox con '{TARGET_MAILBOX}'")
        
        mailbox_ids = [mb[0] for mb in all_target_mailboxes]
        print(f"✓ Encontrados {len(mailbox_ids)} mailboxes con '{TARGET_MAILBOX}'")
        
        # Usar el primer mailbox para obtener la ruta base
        mailbox_url = all_target_mailboxes[0][1].replace('file://', '')
        
        # Buscar mensajes en TODOS los mailboxes objetivo
        placeholders = ','.join('?' * len(mailbox_ids))
        query = f"""
        SELECT DISTINCT
            m.subject,
            m.ROWID as message_id,
            addr.address AS sender_email
        FROM messages m
        LEFT JOIN addresses addr ON m.sender = addr.ROWID
        WHERE addr.address = ?
        AND m.mailbox IN ({placeholders})
        ORDER BY m.date_received DESC
        """
        
        cursor.execute(query, (STREAK_SENDER, *mailbox_ids))
        messages = cursor.fetchall()
        
        print(f"✓ Encontrados {len(messages)} mensajes")
        
        results = []
        mail_base_dir = Path.home() / "Library" / "Mail" / "V10"
        
        for msg in messages:
            subject = clean_text(msg['subject'])
            
            # Buscar el archivo .emlx recursivamente en todo el directorio de Mail
            content = ""
            message_id = msg['message_id']
            emlx_filename = f"{message_id}.emlx"
            
            # Buscar en todo el directorio V10
            emlx_files = list(mail_base_dir.rglob(emlx_filename))
            
            if emlx_files:
                emlx_file = emlx_files[0]
                try:
                    with open(emlx_file, 'r', encoding='utf-8', errors='ignore') as f:
                        # El formato .emlx tiene un número en la primera línea, luego el email
                        lines = f.readlines()
                        if len(lines) > 1:
                            email_content = ''.join(lines[1:])
                            content = extract_plain_text(email_content)
                except Exception as e:
                    content = f"(error leyendo archivo: {e})"
            else:
                content = "(archivo .emlx no encontrado)"
            
            results.append({
                "subject": subject,
                "content": content
            })
        
        # Guardar a JSON
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = Path(__file__).parent / f"Streak-mails-{timestamp}.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Exportados {len(results)} correos a: {output_file}")
        return output_file
        
    finally:
        conn.close()


if __name__ == "__main__":
    try:
        print("🚀 Extrayendo correos de Streak desde Mail.app...")
        print("=" * 60)
        
        # Primero intentar con contenido completo
        print("\n📖 Intentando extraer contenido completo de archivos .emlx...")
        try:
            export_with_full_content()
        except Exception as e:
            print(f"⚠ No se pudo extraer contenido completo: {e}")
            print("\n📝 Usando preview de la base de datos...")
            export_streak_emails()
        
        print("\n✅ Proceso completado")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
