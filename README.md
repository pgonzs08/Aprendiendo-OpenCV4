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

		Para instalar opencv4 en mi sistema operativo -macOS- solo tuve que instalar scipy y opencv utilizando los
	 	comandos pip install scipy y pip install opencv-contrib-python. En el libro enseña como hacerlo sin siquiera
		tener python instalado y dado que ya conozco como utilizar pip lo ignoré. Me planteé usar un docker para man-
		tener la organización pero me temo que ese problema es del Pablo de mañana.

		Una vez instaladas las librerías ejecute el ejemplo del capítulo 2 llamado 0-PngToJpg.py, que crea una copia
		de la imágen MyPic.png en jpg.

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

Día Martes 12 de Septiembre de 2023:

	ACCEDIENDO A DATOS CON NUMPY.ARRAY

	El acceso y la modificación de valores de regiones de interés en un array de numpy se puede realizar a través de indexación
	y las funciones item e itemset. La función item toma como argumentos los índices del valor que deseamos obtener como enteros
	y devuelve el valor, mientras que itemset toma dos argumentos, una tupla con los índices del valor a modificar y el valor por
	el que queremos sustituirlo. Por razones de eficiencia la modificación y obtencion de zonas más grandes es recomendable reali-
	zarlas con funciones de opencv o con array slices de numpy.

Día Miércoles 13 de Septiembre de 2023:

	Los arrays de numpy tienen las propiedades shape, size y dtype que describen la forma del array, la cantidad de elementos que
	contiene y el tipo de datos que guarda, respectivamente. Utilizando estas propiedades podemos modificar las imágenes para pro-
	ducir efectos como los vistos en FotoSimetrica.png generado por AccessingDataWithNP.py. Conocer éstas propiedades es fundamen-
	tal en el tratamiento de imágenes a través de OpenCV.

	LEYENDO Y ESCRIBIENDO ARCHIVOS DE VIDEO

	Quiero mencionar que para la sección de video he utilizado una animación hecha por el grupo de Alejandro Fernández Gómez en la
	asignatura de animación por computador del grado de ingeniería informática en león. 

	Para leer y escribir video opencv proporciona dos clases: VideoCapture y VideoWriter.

	VideoCapture se instancia con el URI del archivo de video a leer. El formato de lectura aceptado puede variar según el OS y la
	build de OpenCV, pero por lo general los video en formato AVI siempre se pueden leer. VideoCapture proporciona el método get pa-
	ra obtener propiedades del vídeo pasándo como argumento un flag que simboliza la propiedad, casi siempre querremos tener los fps
	del video, para lo que utilizaremos el flag cv2.CAP_PROP_FPS, y el tamaño del video, para el que utilizamos 
	cv2.CAP_PROP_FRAME_WIDTH para la hanchura y cv2.CAP_PROP_FRAME_HEIGHT para la altura. El método get siempre devuelve float, así
	que debemos castearlo a otros tipos de datos según nuestras necesidades.

	VideoWriter se instancia con el URI, el codec, los fps y el tamaño del archivo a escribir. El codec que pongamos designará la 
	extensión que debemos utilizar y es un flag que obtendremos con la función cv2.VideoWriter_fourcc(*f"{codec}").

	Para leer el video utilizamos la función read de VideoCapture. Ésta lee frame el siguiente frame del video cada vez que se la
	invoca y no necesita argumentos y nos devuelve dos valores: un booleano que será True si la lectura del frame fue exitosa y 
	el frame leído. Gracias al booleano podemos hacer fácilmente un bucle while que lea el video entero.
	
	De forma análoga el método write de VideoCapture escribe frame por frame el video. El único argumento que necesita es el frame
	a escribir, que será una imágen.
