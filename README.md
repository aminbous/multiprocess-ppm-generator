# multiprocess-ppm-generator

Este proyecto implementa una aplicación en Python que genera múltiples imágenes en formato PPM (P3) de manera concurrente utilizando multiprocesamiento y programación orientada a objetos.

Cada proceso se encarga de crear una imagen de tamaño configurable, rellenando sus píxeles con valores RGB generados aleatoriamente en el rango de 0 a 255. De forma opcional, para alcanzar la máxima calificación, los valores generados pueden ser números primos aleatorios.

Durante la ejecución, los procesos comparten información para calcular de forma sincronizada la media de los valores rojo, verde y azul (RGB) de todas las imágenes generadas, utilizando mecanismos de comunicación entre procesos (IPC) y un objeto de bloqueo para garantizar el acceso seguro a los datos compartidos.

El programa se ejecuta desde la línea de comandos y recibe como parámetros el número de imágenes a generar, así como el ancho y alto de cada una. Cada proceso crea un archivo PPM independiente, nombrado según su identificador (por ejemplo, p1.ppm, p2.ppm, etc.).
