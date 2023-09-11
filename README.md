Día Lunes 11 de Septiembre de 2023:

	He creado un repositorio para aprender OpenCV4 con un libro que he encontrado en la biblioteca
	de la Escuela de Ingeniería Informática Industrial y Aeroespacial de la Universidadd de León.

	Ya tengo conocimientos previos de Python y he utilizado una versión anterior de OpenCV en mi
	formación. Tengo el objetivo de refinar mi conocimiento sobre ésta y adquirir conocimientos
	prácticos de visión por computador.

	-----------------------------------------------------------------------------------------------

	Para comenzar a trabajar he clonado el repositorio proporcionado por el libro:

		 https://github.com/PacktPublishing/Learning-OpenCV-4-Computer-Vision-with-Python-Third-Edition.git

	En él hay código de ejemplo que servirá para guiar el aprendizaje.

	-----------------------------------------------------------------------------------------------

	Capítulo 1:

		Para instalar opencv4 en mi sistema operativo -macOS- solo tuve que instalar scipy y opencv utilizando los comandos pip install scipy y pip install opencv-contrib-python. En el libro enseña como hacerlo sin siquiera tener python instalado y dado que ya conozco como utilizar pip lo ignoré. Me planteé usar un docker para mantener la organización pero me temo que ese problema es del Pablo de mañana.

		Una vez instaladas las librerías ejecute el ejemplo del capítulo 2 llamado 0-PngToJpg.py, que crea una copia de la imágen MyPic.png en jpg.

	-----------------------------------------------------------------------------------------------

	Capítulo 2:

		En éste capítulo se cubre:

		- La lectura de imágenes de archivos de imagen, video, cámaras o bytes de memoria
		- Escritura de imágenes en archivos de imagen o video
		- Manipulación de datos de imagen con NumPy
		- Mostrar imágenes en ventanas
		- Tratamiento de eventos de ratón y teclado
		- Implementación de una aplicación con diseño orientado a objetos


	LECTURA Y ESCRITURA		

	La lectura y escritura de imágenes en opencv se realiza a través de las funciones imread y imwrite. 
	La función imread toma como argumento posicional el URI del archivo de imagen a leer que en la build estandar debe estar en formato
	tiff, jpg, png o bmp. También tiene un argumento clave opcional llamado flags que indica el modo de lectura
	de la imágen, que de predeterminado lee a color. Invocarlo devolverá una representación en un array de numpy
 	dependiente del modo de lectura que por determinado tendrá dimensiones (altura, hanchura, 3).

	Las imágenes de opencv siempre se representan como arrays multidimensionales cuya tercera dimensión es dependiente
	del modo de representar el color de los píxeles, puede ser escala de grises teniendo un solo canal, RGB, BGR o HSV 
	con tres e incluso RGBA o BGRA con cuatro.

	La función imwrite toma como argumentos el URI del archivo de imágen en el que se guardará la imágen que se pasa
	como segundo argumento en forma de array de numpy. Es necesario que el tipo de dato que guarda el array de numpy coincida
	con el formato en el que se desea guardar la imagen.


	REPRESENTACIÓN EN BYTEARRAY

	Los valores de los canales son normalmente representados  on enteros entre 0 y 255, o lo que es lo mismo enteros de
	8 bits o bytes. Por tanto la transformación entre imágenes de opencv y bytearrays de python es directa.
