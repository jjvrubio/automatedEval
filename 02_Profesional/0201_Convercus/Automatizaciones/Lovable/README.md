# Guía de trabajo: Convercus y Lovable

## Propósito

Este documento resume cómo utilizar Lovable para crear una simulación de la aplicación de Convercus y cómo puede ayudar Codex durante el diseño, la integración y la evolución del proyecto.

La aplicación tiene como objetivo mostrar una experiencia móvil con cupones, noticias, puntos, niveles, movimientos y elementos de gamificación. La primera fase está orientada a una demostración funcional y visual, con posibilidad de evolucionar posteriormente hacia un producto conectado a datos reales.

## Decisión sobre la plataforma

Lovable no se descarta. Para la fase actual es probablemente la opción más adecuada porque permite:

- Crear rápidamente una demostración visual y navegable.
- Diseñar una aplicación web *mobile-first* con apariencia de app.
- Compartir el resultado mediante una URL.
- Integrar APIs públicas o privadas.
- Utilizar datos simulados mientras se completa la integración.
- Sincronizar el código con GitHub cuando sea necesario.
- Extraer el código y desplegarlo fuera de Lovable en el futuro.

La principal diferencia frente a FlutterFlow es el objetivo del producto:

| Plataforma | Uso recomendado |
|---|---|
| Lovable | Prototipo web *mobile-first*, demostración comercial e iteración rápida |
| FlutterFlow | Aplicación móvil nativa orientada a publicación en App Store y Google Play |
| Figma | Prototipo exclusivamente visual, sin integración funcional con la API |

La recomendación actual es continuar con Lovable. Solo tendría sentido reconsiderar FlutterFlow si se decide que la siguiente fase debe ser una aplicación móvil nativa o si la gestión de la API desde Lovable se vuelve innecesariamente compleja.

## Cómo puede ayudar Codex

### Producto y experiencia de usuario

Codex puede:

- Definir la arquitectura funcional de la aplicación.
- Diseñar la navegación y los flujos principales.
- Traducir los objetivos comerciales a requisitos concretos.
- Proponer estados de carga, error, vacío y ausencia de conexión.
- Diseñar una estrategia gradual entre datos simulados y datos reales.
- Preparar el guion de una demostración comercial.

### Trabajo con Lovable

Codex puede:

- Redactar un prompt maestro para iniciar o reorganizar el proyecto.
- Preparar prompts pequeños y verificables para cada pantalla.
- Revisar las respuestas de Lovable y corregir instrucciones ambiguas.
- Diagnosticar problemas en el código generado.
- Mejorar la estructura TypeScript, los componentes y los servicios de API.
- Revisar capturas, mensajes de error y fragmentos de código.
- Trabajar directamente sobre el repositorio cuando se active la sincronización con GitHub.

### Integración con Convercus

Codex puede:

- Analizar la documentación OpenAPI de Convercus.
- Seleccionar los endpoints necesarios para cada pantalla.
- Identificar parámetros, cabeceras y modelos de respuesta.
- Crear tipos TypeScript para las respuestas de la API.
- Preparar servicios, adaptadores y Edge Functions.
- Diagnosticar errores de autenticación, CORS o transformación de JSON.
- Evitar que tokens y credenciales queden expuestos en el navegador.

## Flujo de trabajo recomendado

1. Definir las pantallas y el alcance de la demostración.
2. Construir la navegación y el sistema visual con datos simulados.
3. Crear una capa de servicios independiente de los componentes visuales.
4. Integrar primero el inicio de sesión y el perfil.
5. Sustituir progresivamente los datos simulados de puntos, cupones, noticias y movimientos.
6. Añadir estados de carga, error y sesión caducada.
7. Validar la experiencia completa con una cuenta de staging.
8. Preparar un recorrido controlado para la demostración.

Esta secuencia permite mantener una demo estable aunque alguno de los servicios de staging no esté disponible.

## Arquitectura recomendada

```text
Interfaz mobile-first en Lovable
            |
            v
Capa de servicios y adaptadores TypeScript
            |
            v
Edge Functions / proxy seguro
            |
            v
API de staging de Convercus
```

Los componentes visuales no deberían conocer directamente la estructura completa de la API. La capa de adaptadores debe transformar las respuestas de Convercus en modelos sencillos para la interfaz, por ejemplo `UserSummary`, `CouponCard`, `NewsItem` y `ActivityItem`.

## Documentación de la API de Convercus

- Swagger UI: <https://staging.convercus.io/api-docs/swagger-ui.html>
- Índice de recursos: <https://staging.convercus.io/api-docs/swagger-resources>
- Autenticación: <https://staging.convercus.io/auth/docs/v2/api-docs>
- Cuentas: <https://staging.convercus.io/accounts/docs/v2/api-docs>
- Cupones: <https://staging.convercus.io/coupons/docs/v2/api-docs>
- Noticias: <https://staging.convercus.io/newsfeed-service/docs/v2/api-json>
- Programas y niveles: <https://staging.convercus.io/programs/docs/v2/api-docs>

Aunque el índice de Swagger etiqueta algunos recursos como Swagger 2.0, los principales documentos analizados declaran OpenAPI 3.0.x.

## Mapa inicial de endpoints

| Función | Método y endpoint | Uso previsto |
|---|---|---|
| Inicio de sesión | `POST /auth/login` | Obtener el token de sesión |
| Perfil completo | `GET /v3/accountdetails/{accountId}` | Resumen del usuario, saldo, nivel y membresías |
| Saldo | `GET /accounts/{accountId}/balance` | Mostrar puntos disponibles y bloqueados |
| Cupones del usuario | `GET /v2/accounts/{accountid}/accountcoupons` | Listado personalizado de cupones |
| Detalle de cupón | `GET /v2/accountcoupons/{accountcouponid}` | Condiciones y estado del cupón |
| Código del cupón | `GET /v2/accountcoupons/{accountcouponid}/code` | Mostrar el código para su uso |
| Canje | `PATCH /v2/accountcoupons/{accountcouponid}` | Canjear un cupón |
| Noticias y actividad | `GET /newsfeed-service/v2/newsfeeds` | Portada y feed personalizado |
| Detalle de noticia | `GET /newsfeed-service/v3/newsfeeds/{newsFeedItemId}` | Vista completa de una publicación |
| Movimientos | `GET /v2/accounts/{accountId}/transactions` | Historial de puntos y transacciones |
| Nivel | `GET /accounts/{accountId}/level` | Estado y progreso del usuario |

## Autenticación

El login espera un cuerpo equivalente a:

```json
{
  "userName": "usuario",
  "password": "contraseña",
  "org": "organización",
  "deviceId": "identificador-opcional"
}
```

`userName`, `password` y `org` son obligatorios. La respuesta correcta devuelve el token como texto. Las operaciones autenticadas utilizan una cabecera Bearer y, en numerosos endpoints personalizados, una cabecera `interaction-id`:

```http
Authorization: Bearer TOKEN
interaction-id: IDENTIFICADOR
```

Las credenciales y los tokens sensibles no deben incluirse en el código del frontend. El login y las llamadas autenticadas deberían ejecutarse en una Edge Function o proxy seguro.

## Información disponible para la interfaz

### Cuenta

El detalle de cuenta ofrece, entre otros:

- Saldo de puntos y puntos bloqueados.
- Nivel y *rating level*.
- Membresías.
- Identificadores.
- Propiedades personalizadas.
- Estado de la cuenta.

### Cupones

Los cupones pueden incluir:

- Nombre y títulos traducidos.
- Imágenes.
- Fechas de validez.
- Tipo y valor del beneficio.
- Estado y disponibilidad para canje.
- Límites y número de canjes.
- Establecimientos o puntos de canje.
- Código promocional.

### Noticias y actividad

El *newsfeed* admite elementos de tipo:

- `POST`
- `EARN_TRANSACTION`
- `BURN_TRANSACTION`
- `CHECKOUT`

Esto permite presentar noticias, compras y movimientos de puntos dentro de una misma experiencia.

### Gamificación

La API ofrece puntos, niveles, *rating levels*, movimientos y reservas de nivel. En la revisión inicial no se ha identificado un servicio específico de misiones, retos o insignias.

Para la primera versión se recomienda:

- Utilizar datos reales para puntos, nivel, movimientos y cupones.
- Simular retos, insignias y barras de progreso.
- Investigar posteriormente si los retos pueden modelarse mediante propiedades personalizadas o configuración de programa.

## Pantallas propuestas

1. Inicio de sesión.
2. Inicio personalizado con puntos, nivel y elementos destacados.
3. Listado de cupones.
4. Detalle y código de cupón.
5. Noticias y actividad.
6. Detalle de noticia.
7. Retos y recompensas simulados.
8. Historial de movimientos.
9. Perfil y membresía.

La navegación inferior inicial puede contener: `Inicio`, `Cupones`, `Retos` y `Perfil`.

## Prompt maestro inicial para Lovable

```text
Crea una aplicación web mobile-first para Convercus.

Objetivo:
Mostrar cupones, noticias, puntos, retos, recompensas y actividad
personalizada de un usuario.

Diseño:
- Apariencia de aplicación móvil.
- Navegación inferior: Inicio, Cupones, Retos y Perfil.
- Tarjetas visuales con bordes redondeados.
- Estados de carga mediante skeletons.
- Estados vacíos y mensajes de error.
- Diseño responsive para móvil y escritorio.

Arquitectura:
- Usar React y TypeScript.
- Separar los servicios de API de los componentes visuales.
- Crear tipos para todas las respuestas.
- No incluir tokens ni secretos en el frontend.
- Utilizar una Edge Function para las llamadas autenticadas.
- Permitir cambiar entre datos simulados y API real.
- Transformar las respuestas externas mediante adaptadores antes de
  entregarlas a los componentes.

Proceso:
- No implementar todos los módulos a la vez.
- Crear primero la estructura, navegación, sistema visual y datos simulados.
- Mantener cada cambio pequeño y verificable.
```

Antes de utilizar este prompt conviene añadir las referencias visuales de marca, colores, tipografías y capturas que deban inspirar el resultado.

## Datos necesarios para activar la API real

Para realizar pruebas completas en staging serán necesarios:

- Usuario de prueba.
- Contraseña de prueba, introducida únicamente como secreto.
- Código de organización (`org`).
- `accountId` o identificador equivalente.
- `interaction-id` válido.
- Idioma de la interfaz, previsiblemente `es`.
- Confirmación de qué operaciones de escritura pueden ejecutarse en staging.

No deben probarse operaciones de canje, modificación o eliminación hasta confirmar que la cuenta y los datos de staging pueden alterarse con seguridad.

## Próximos pasos

1. Revisar el proyecto actual de Lovable mediante capturas o URL de previsualización.
2. Documentar las pantallas que ya existen y su estado.
3. Ajustar el prompt maestro a la identidad visual de Convercus.
4. Crear un mapa detallado entre campos de API y componentes de pantalla.
5. Implementar primero el modo simulado.
6. Activar la integración con staging por módulos.
7. Conectar GitHub cuando sea útil revisar o modificar directamente el código generado.
