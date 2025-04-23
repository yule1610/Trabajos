************************************************************************************************************************************************************************************************************************************************
Piedra, Papel o Tijeras

Este es un juego basado en el clásico concepto de “Piedra, Papel o Tijeras”. Permite al usuario seleccionar una de las tres opciones disponibles, mientras que el sistema, mediante el uso de estructuras condicionales y una función aleatoria
(random), genera automáticamente la elección de la máquina. Esto asegura que cada partida sea impredecible y dinámica.

************************************************************************************************************************************************************************************************************************************************
Hangman.py

Este es un juego de tipo "Ahorcado", en el cual el jugador debe adivinar una palabra secreta letra por letra. Si la letra ingresada se encuentra en la palabra,
se revela en todas las posiciones correspondientes; en caso contrario, el jugador pierde un intento. El juego continúa hasta que se adivina la palabra completa o se agotan los intentos.
La palabra se selecciona de forma aleatoria desde una lista definida, lo que garantiza una experiencia distinta en cada partida. El jugador también recibe retroalimentación constante sobre las letras utilizadas y los intentos restantes.

Especificaciones Técnicas

Este programa utiliza los siguientes conceptos de programación:
Importación de módulos: Se utiliza el módulo random para seleccionar una palabra al azar.
Listas: Se maneja una lista de palabras posibles.
Conjuntos (sets): Para almacenar letras usadas y letras por adivinar, optimizando las búsquedas.
Condicionales (if, elif, else): Para manejar la lógica de decisiones del juego.
Bucles (while): Para mantener el juego en ejecución hasta que se cumpla una condición de fin.
Funciones (def): Todo el juego está contenido en una función llamada hangman().
Entrada del usuario (input): Para capturar las letras que el jugador desea adivinar.
Manejo de cadenas y listas: Para mostrar el progreso de la palabra y las letras adivinadas correctamente.

************************************************************************************************************************************************************************************************************************************************
Temporizador de cuenta regresiva


Este es un generador automático de contraseñas seguras y aleatorias. El programa crea combinaciones de caracteres que incluyen letras mayúsculas, letras minúsculas, números y símbolos especiales. 
Se garantiza que cada contraseña generada contenga al menos un carácter de cada tipo para cumplir con los estándares básicos de seguridad.
El sistema genera dos contraseñas independientes de una longitud determinada (en este caso, 8 caracteres), asegurando que ambas sean distintas y difíciles de adivinar mediante técnicas comunes de ataque como fuerza bruta.

Especificaciones Técnicas

Este programa emplea los siguientes elementos y conceptos de programación:
Importación de módulos:
string: Para acceder fácilmente a conjuntos de caracteres como letras, dígitos y símbolos.
random: Para seleccionar elementos al azar y mezclar la contraseña.
secrets: Para realizar selecciones aleatorias más seguras desde el punto de vista criptográfico.
Concatenación de caracteres: Se crea una cadena combinando letras (mayúsculas y minúsculas), dígitos y símbolos especiales.
Listas: Se utiliza una lista para construir la contraseña carácter por carácter antes de convertirla en una cadena.
Funciones de selección aleatoria:
random.choice(): Para asegurar que la contraseña contenga al menos una letra minúscula, una mayúscula, un número y un símbolo.
secrets.choice(): Para seleccionar los caracteres restantes de forma segura.
random.shuffle(): Para mezclar los caracteres y garantizar que el orden no sea predecible.
Bucles while: Para completar la longitud deseada de la contraseña.
Conversión de lista a cadena: Se utiliza "".join() para convertir la lista de caracteres en una cadena lista para su uso.
Impresión de resultados (print): Para mostrar las contraseñas generadas al usuario.

************************************************************************************************************************************************************************************************************************************************
Códigos QR

Este es un generador de códigos QR que permite codificar información en un formato visual legible por dispositivos como teléfonos móviles o escáneres de QR. 
En este caso, el programa genera un código QR en formato ASCII (texto plano) que representa la información suministrada, ideal para mostrarlo directamente en una terminal o consola.
El contenido codificado es el texto "Yuleisi Montero", pero puede adaptarse fácilmente para cualquier otra cadena de texto, enlace o dato que se desee codificar.

Este programa hace uso de los siguientes elementos y técnicas de programación:
Librerías externas:
qrcode: Librería especializada para generar códigos QR.
io: Módulo estándar utilizado para manejar flujos de entrada/salida en memoria (en este caso, para capturar la salida ASCII del QR).

Instancia de QR:
Se crea un objeto QRCode() que representa el código QR a generar.
Método add_data():
Se utiliza para agregar el contenido que se desea codificar en el código QR.
Impresión ASCII del código QR:
El método print_ascii() imprime una versión del QR en caracteres ASCII (texto plano), útil para mostrar en consola.
Manejo de flujo de texto:
Se emplea io.StringIO() para capturar y manipular la salida del QR como si fuese un archivo de texto.
Lectura y visualización:
Se imprime el contenido almacenado en el buffer para mostrar el QR en la terminal.

************************************************************************************************************************************************************************************************************************************************
Generador de contraseñas

Este es un generador automático de contraseñas seguras y aleatorias. El programa crea combinaciones de caracteres que incluyen letras mayúsculas, letras minúsculas, números y símbolos especiales. 
Se garantiza que cada contraseña generada contenga al menos un carácter de cada tipo para cumplir con los estándares básicos de seguridad.
El sistema genera dos contraseñas independientes de una longitud determinada (en este caso, 8 caracteres), asegurando que ambas sean distintas y difíciles de adivinar mediante técnicas comunes de ataque como fuerza bruta.

Especificaciones Técnicas
Este programa emplea los siguientes elementos y conceptos de programación:

string: Para acceder fácilmente a conjuntos de caracteres como letras, dígitos y símbolos.
random: Para seleccionar elementos al azar y mezclar la contraseña.
secrets: Para realizar selecciones aleatorias más seguras desde el punto de vista criptográfico.
Concatenación de caracteres: Se crea una cadena combinando letras (mayúsculas y minúsculas), dígitos y símbolos especiales.
Listas: Se utiliza una lista para construir la contraseña carácter por carácter antes de convertirla en una cadena.
Funciones de selección aleatoria:
random.choice(): Para asegurar que la contraseña contenga al menos una letra minúscula, una mayúscula, un número y un símbolo.
secrets.choice(): Para seleccionar los caracteres restantes de forma segura.
random.shuffle(): Para mezclar los caracteres y garantizar que el orden no sea predecible.
Bucles while: Para completar la longitud deseada de la contraseña.
Conversión de lista a cadena: Se utiliza "".join() para convertir la lista de caracteres en una cadena lista para su uso.
Impresión de resultados (print): Para mostrar las contraseñas generadas al usuario.

************************************************************************************************************************************************************************************************************************************************
Juego de tic-tac-toe

Este proyecto consiste en un juego clásico de Tic Tac Toe (Tres en Raya), desarrollado utilizando Python. El juego cuenta con una interfaz gráfica que permite a dos jugadores turnarse para marcar sus movimientos en un tablero de 3x3.
El objetivo es lograr alinear tres símbolos iguales, ya sea en forma horizontal, vertical o diagonal. El juego detecta automáticamente cuándo uno de los jugadores gana y permite reiniciar la partida.

Especificaciones del código:
Librería usada para la interfaz gráfica: Tkinter
Disposición del tablero hecha con el método grid()
Control del flujo del juego a través de funciones como:
controlTurno() para alternar entre los turnos de cada jugador.
revisarGanador() para verificar si algún jugador ha ganado la partida.
Limpiar() para reiniciar el tablero.
Se usaron StringVar para actualizar dinámicamente el texto de los botones.
Implementación de condiciones para evitar que los jugadores sobrescriban una casilla ya ocupada.
El juego desactiva el tablero al finalizar con una victoria para evitar más movimientos.
Estilo visual sencillo y funcional, adecuado para un entorno de aprendizaje o demostración de lógica básica en programación.

************************************************************************************************************************************************************************************************************************************************
Lista de tareas con Flask y JSON

Este código crea una API utilizando Flask, un microframework para Python, que permite gestionar una lista de tareas. La aplicación tiene dos rutas principales: una para obtener las tareas existentes y otra para agregar nuevas tareas a la lista.

Descripción de la funcionalidad:
Ruta GET (/items):
Método: GET
Descripción: Permite obtener la lista actual de tareas en formato JSON.
Respuesta: La API responderá con la lista de tareas que contiene elementos como "Estudiar matemáticas", "Hacer ejercicio", "Leer un libro", entre otros.

Ruta POST (/items):
Método: POST
Descripción: Permite agregar una nueva tarea a la lista de tareas. El cliente debe enviar un objeto JSON con un campo "tarea" que contenga el texto de la nueva tarea.
Validación: Si la solicitud no incluye el campo "tarea", la API responderá con un error 400 indicando que el formato de la solicitud es incorrecto.
Respuesta: Si la tarea es válida, se agrega a la lista y la respuesta incluirá un mensaje de éxito, junto con la lista actualizada de tareas.

Flujo de la aplicación:
Inicialización de la aplicación Flask: Se crea una instancia de Flask para manejar las solicitudes HTTP.
Definición de datos: Se define una lista llamada data que contiene algunas tareas de ejemplo.
Rutas definidas:

GET /items: Devuelve la lista de tareas en formato JSON.
POST /items: Permite agregar una nueva tarea a la lista, siempre y cuando el cuerpo de la solicitud contenga un campo "tarea".

Tuve que instalar: Flask
