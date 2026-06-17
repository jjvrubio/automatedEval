Quiero crear un script en python para revisar las palabras clave que ha elegido el alumno para facilitar localizar su TFE entre una miríada de parecidos. Y, en segundo lugar, para que los lectores puedan discriminar el interés temático que aporta su TFE.

Uso Mac OS y quiero emplear la UI de AppKit para la selección del TFE, en formato PDF o DOCX.

Hay una sección párrafo que comienza por “Palabras clave:” al que le sigue una secuencia de palabras clave separadas por comas y que finaliza en un punto. Hay una sección análoga que comienza por “Keywords” que es aversión en inglés de las palabras claves elegidas. Los alumnos siempre eligen palabras clave muy poco apropiadas que no cumplen la funcionalidad arriba descrita.

Quiero que sigas la siguiente secuencia de instrucciones:

1. Se pueda seleccionar el archivo del TFE mediante interfaz visual (appkit).
2. Extraer las palabras clave.
3. Usar la API de OpenAI 
   1. A la que enviar el PDF para que lo examine
   2. Devuelva las 6 palabras clave idóneas.
   3. La explicación de la selección.
4. Escribir esta respuesta en un archivo markdown en la misma carpeta desde la que se ha seleccionado el TFE.