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
	asignatura de animación por computador del grado de ingeniería informática en león. Su github es: https://github.com/aljfergo. 

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

Día Jueves 14 de Septiembre de 2023:

	CAPTURANDO FRAMES DE LA CÁMARA:

	Para capturar frames de una cámara utilizamos VideoCapture, pero en lugar de poner el URI de un archivo de video pasamos como argumento
	el índice de la cámara a capturar. Extraer las características de la cámara no es tan sencillo como extraerlas de un archivo de video.
	Intentar obtener el framerate de una cámara con VidoeCapture.get normalmente devolverá 0 y en algunas ocasiones aunque devuelva un valor
	éste será distinto a los fps, por tanto al capturar de la cámara debemos asumir ésta caracterísitca o medirla. 

	Las dimensiones de la imágen obtenidas a través de VideoCApture.get también pueden no ser precisas, una medida precisa de obtener tales
	dimensiones es extraerlas de un frame leído con éxito. Otra fuente de problemas respecto a las dimensiones de la cámara es que algunas
	cámaras graban de manera inestable al encenderlas y los frames que extraen tienen dimensiones distintas. Éste problema se puede resolver
	ignorando los primeros frames que se lean de tales cámaras.

	MOSTRANDO UNA IMÁGEN EN UNA VENTANA

	Para mostrar una imágen en una ventana opencv nos proporciona la función imshow, que toma como argumentos el nombre de la ventana en forma
	de string y la imágen a mostrar. Cuando se ejecute, se abrirá una ventana cuando se llame a la función de opencv waitKey. La función waitKey
	tiene un argumento opcional entero. Éste argumento dicta cuánto tiempo en milisegundos va a esperar la función y devolverá cualquier tecla 
	pulsada en éste periodo. Si no se pasa ningún argumento se dejará de esperar al pulsar la primera tecla. Cuando acaba el periodo de espera 
	sin que se haya pulsado ninguna tecla devuelve -1.

	Otra función importante a la hora de manejar ventanas en opencv es destroyAllWindows, que cierra todas las ventanas que han sido creadas por 
	opencv.

	MOSTRANDO FRAMES DE LA CÁMARA EN UNA VENTANA

	Uniendo todo podemos crear un programa que muestre el video capturado por la cámara en directo. Para ello tenemos que tener en cuenta que llamar
	a imshow redibuja las ventana pasada como argumento si ésta ya está abierta, actualizando la imágen que muestra, pero nunca antes de invocar a 
	waitKey.

	Para ésta sección es relevante hablar de la programación orientada a eventos en opencv. La función namedWindow de opencv abre una ventana nombrada
	con el argumento que le pasemosa a la que podemos asignar manejadores de eventos con funciones como setMouseCallBack, que toma como argumentos
	el nombre de la ventana a la que queremos asignar la manejadora y la propia función manejadora del evento. Las funciones manejadores que pasemos a
	setMouseCallback deben de aceptar los argumentos posicionales event, x, y, flags y param.

	Los argumentos event y flag de las manejadores de setMouseCallback nos indican qué acción se ha cometido exactamente con el ratón y en qué condi-
	ciones, respectivamente.

	Las opciones de manejo de eventos en ventans son limitadas y por tanto se suele integrar opencv en otros frameworks

Día Viernes 15 de Septiembre de 2023

	PROYECTO CAMEO: SEGUIMIENTO DE CARAS Y MANIPULACIÓN DE IMÁGENES

	OpenCV se estudia como un libro de recetas en el que se cubren una gran variedad de algoritmos, pero nada sobre el desarrollo de aplicaciones
	a alto nivel debido a la gran diversidad de aplicaciones potenciales de ésta biblioteca. En éste libro los autores creen que se puede aprender
	OpenCV creando aplicaciones en las que se implementen ejemplos en componentes extensibles y reusables.

	La aplicación que se desarrolla en ésta sección es una aplicación interactiva que realiza seguimiento facial y manipulación de imágenes en in-
	puts de la cámara en tiempo real.

	Específicamente la aplicación mezclará caras en tiempo real, dados dos treams de cámara, la aplicación superpondrá caras de un stream sobre
	caras del otro. Se aplicarán filtros y distorsiones para dar a ésta escena mezclada un aspecto y sensación unificados. Los usuarios deben te-
	ner la experiencia de estar inmersos en un espectáculo en vivo donde entran otro entorno y personaje. Una experiencia popular en parques de
	atracciones como Disneylandia.

	Se probarán distintas estrategias con el fin de minimizar los fallos notables por los usuarios. La aplicación se llamará Cameo.

	CAMEO - DISEÑO ORIENTADO A OBJETOS

	Con el fin de promover la modularidad y la accesibilidad la aplicación se desarrollará Orientada a Objetos. Crearemos las clases CAptureMana-
	ger y WindowManager como interfaces I/O de alto nivel. CaptureManager tendrá la misión de leer nuevos frames y opcionalmente mandar ese frame
	a uno o más outputs entre los que se incluirán ventanas (A través de WindowManager), archivos de video y archivos de imágen. WindowManager ten-
	drá la misión de manejar una ventana y eventos en estilo orientado a objetos.
	
	Ambas clases son extensibles. Debemos hacer implementaciones que no sean dependientes de I/O de OpenCV.

	
	-----------------------------------------------------------------------------------------------

Día Sábado 16 de Septiembre de 2023

	Capítulo 3:

		Éste capítulo cubre:

		- Convertir imágenes entre diferentes modelos de colores
		- Entender la importancia de las frecuencias y la transformada de Fourier en procesamiento de imágenes
		- Aplicar filtros de paso alto (HPFs), filtros de paso bajo (LPFs), filtros de detección de bordes y filtros de convolución customizados
		- Detectar y analizar contornos, líneas, círculos y otras formas geometricas
		- Escribir Clases y funciones que encapsulen la implementación de un filtro

	Para éste capítulo se usan las librerías OpenCv, Numpy y Scipy.

	CONVIRTIENDO IMÁGENES ENTRE DIFERENTES MODELOS DE COLOR

	OpenCV implementa cientos de fórmulas relacionadas con la conversión entre modelos de colores. Algunos modelos de colores son usados comúnmente
	por dispositivos de input domo cámaras, miento que otros modelos son usados por dispositivos de output como impresoras y pantallas. La Visión por
	computador suele trabajar con tres modelos de colores: grayscale, BGR y HSV (escala de grises, azul-verde-rojo, tono-saturación-valor):

	· Grayscale es un medole que reduce la informacín de color traduciéndola en sombras de gris o luminosidad. Éste modelo es extremadamente útil
	para el procesamiento intermedio de imágenes en problemas donde la información de luminosidad por sí sola es suficiente, como detección de rostros.
	Típicamente, cada pixel en escala de grises es representado po un único valor de 8 bits, desde el 0 para el negro hasta el 255 para el blanco.

	· BGR es el modelo de color azul-verde-rojo, en el que cada pixel tiene un triplete de valores representando los componentes azul, verde y rojo 
	o cada canal de color. Los desarrolladores web, y cualquiera que trabaje con gráficos por computador, está familiarizado con una definición similar,
	excepto con el orden de los canales invertidas. Típicamente, cada pixel en BGR es representado por una tripleta de valores como [0,0,0] para el ne-
	gro, [255, 0, 0] para el azul, [0,255,0] para el verde, [0,0,255] para el rojo y [255,255,255] para el blanco.

	· El modelo HSV usa una tripleta de canales diferentes que representan el tono del color, la intensidad y el brillo.

	Por defecto OpenCV utiliza el modelo BGR para representar cualquier imagen que cargue de un archivo o capture de una cámara.

	LA LUZ NO ES PINTURA

	El modelo de colores BGR se diferencia de la pintura normal en que mezclar colores en pintura se considera substractivo y en OpenCV mezclar colores
	es aditivo, por eso la tripleta [0,255,255] (0 azul, máximo verde, máximo rojo) da amarillo.

	EXPLORANDO LA TRANSFORMADA DE FOURIER

	Gran parte del procesado aplicado a imágenes y videos en OpenCV tiene que ver con el concepto de la Transformada de Fourier en alguna medida. Joseph
	Fourier fue un Matemática Francés del sifo XVIII que descubrió y popularizó muchos conceptos matemáticos. Estudió la física del calor y las matemá-
	ticas de todas las cosas que pueden ser representadas por funciones de onda. En particular, observó que todas las onas son sólo la suma de funciones
	sinusoides simples de diferentes frecuencias.

	En otras palabras, las ondas que observas y olles a tu alrededor son la suma de otras ondas. Éste concepto es increíblemente útil al manipular imáge-
	nes porque nos permite identificar regiones donde una señas, como los valores de los píxeles, camvia mucho y regiones donde no cambia tanto. Podemos
	marcar arbitrariamente esta refiones como ruido o como refiones de interés, fondo u objeto, y más. Éstas son las frecuencias que hacen la imágen ori-
	ginal, y tenemos el poder de separarlas para extrapolar datos interesantes de la imágen de forma que el ordenador lo pueda comprender.

	Examinemos el concepto de espectro de magnitudas de una imágen usando la transformada de Fourier. El espectro de magnitudes de una imagen es otra i-
	magen qie provee una representación de la imágen original en términos de sus cambios.

	La transformada de Fourier es la base de muchos algoritmos que se usan para operaciones comunes de procesado de imágenes, como detección de bordes,
	líneas o formas.

	HPFS Y LPFS

	Un filtro HPF examina una región de una imagen y potencia la intensidad de los píxeles basada en la diferencia de intensidad de sus vecinos.

	Un filtro LPF examina una región de una imagen y lo suaviza si la diferencia con sus vecinos es menor que un cierto threshold.

	Para aprender más de filtros para la convolución y la correlación recomiendo personalmente leer:
		 Correlation and Convolution. Class Notes for CMSC 426, Fall 2005 David Jacobs

	En ese paper se entra en más profundidad en la naturaleza de las operaciones de convolución y correlación (las operaciones que se realizan para apli-
	car los filtros nombrados), filtros customizados basados en la campana de Gauss, algoritmos eficientes y las series de Fourier.

Día Lunes 18 de Septiembre de 2023

	Las funciones de opencv y scipy que nos permiten aplicar filtros son:

	cv2.GaussianBlur: Toma como argumentos la imagen, el tamaño del kernel Gaussiano, los valores sigmaX y sigmaY (David Jacobs) y borderType, que es un
	un flag para decidir qué padding utilizar en los bordes de la imagen.

	ndimage.convolve: Toma como argumentos la imagen y el kernel de convolución 2D

	cv2.filter2D: Una imágen y un kernel de convolución 2D

	cv2.sepFilter2D: Una imágen y dos kernel de convolución 1D que conforman un kernel de convolución 2D juntos (razones para esto también en David Jacobs)

	CREANDO MÓDULOS

	Vamos a modificar el proyecto Cameo empezado en el capítulo2 para que aplique filtros a las imágenes capturadas en tiempo real. Los filtros tienen que
	poder ser reusados fuera de Cameo. Creamos los archivos filters.py y utils.py donde guardaremos filtros y funciones matemáticas de propósito general,
	respectivamente.
	
Día Viernes 22 de Septiembre de 2023

	KERNELS CUSTOMIZADOS - PONIÉNDONOS CONVOLUCIONADOS

	En éste apartado se habla de cómo funciona la función filter2D introduciéndonos a unas pinceladas de qué es una convolución y explicándo más argumentos
	de la función.

	filter2D(src, -1, kernel, dest): src es la imágen original sobre la que se aplicará una convolución usando kernel. dest es la imágen de destino en la que
	se guardará el resultado de la convolución y el segundo argumento especifíca la profundidad por canal de la imagen destino (cantidad de bits por canal). 
	El valor negativo indica que la imagen de destino debe tener la misma profundidad que la imagen de origen.

	En base a éste ejemplo añadimos dos nuevas clases a filters.py:

	VConvolutionFiler que aplica una convolución a V (o todos los canales)

	SharpenFilter(VConvolutioFilter) un filtro de afilado con un radio de un pixel. En ésta clase los valores del HPF aplicados suman a 1 de forma que podemos
	mantener el color de la imágen.

	Por si queremos crear una máscara que encuentre los bordes de una imágen creamos la clase

	FindEdgesFilter(VConvolutionFilter) que hace lo mismo que Sharpen filter salvo por que la suma de los valores de su filtro asociado son 0 y por tanto los
	borden quedan en blanco y los no bordes en negro.

	También añadimos un filtro de desenfoque:
	BlurFilter(VConvolutionFilter) un filtro de desenfoque con dos píxeles de radio
	
	Y un filtro de realzado
	EmbossFilter(VConvolutionFilter)
	
	MODIFICANDO LA APLICACIÓN:

	Ahora en el archivo cameo.py debemos importar filters e inicializar los filtros que usemos dontro de la clase Cameo. En el bucle principal es trivial aplicar
	el filtro a los frames que capturemos.

Día Lunes 25 de Septiembre de 2023

	DETECCIÓN DE BORDES CON CANNY

	OpenCv ofrece una función llamada Canny (por el inventor del algoritmo John F. Canny) muy popular no sólo por su efectividad si no por la simpricidad de imple-
	mentación en un entorno con OpenCV ya que se escribe en una sola línea:

	cv2.Canny(img, 200, 300) por ejemplo.

	El algoritmo Canny consiste en 5 pasos:
	
	1. Quitar el ruido con un filtro Gaussiano
	2. Calcular los gradientes
	3. Aplicar NMS a los bordes (Se explica en profundidad en el capítulo 7)
	4. Aplicar un threshold doble para todos los bordes detectados para eliminar falsos positivos
	5. Analizar todos los bordes y su conexión uno a otro para descartar bordes débiles

	Los bordes detectados por Canny pueden ser analizados para comprobar si se unen en una figura común.

Día Miércoles 27 de Septiembre de 2023

	DETECCIÓN DE CONTORNOS

	Una tarea vital en la visión por computador es la detección de contornos. Queremos detectar contornos o líneas divisoras de sujetos contenidos en una imágen o el
	frame de un video, no sólo como un fin por sí mismo si no como un paso hacia otras operaciones. Éstas operaciones son computar polígonos circunscritos, aproximar
	formas y calcular regiones de interés. Las regiones de interés simplifican la interacción con datos de imagen porque una región rectangular en NumPy es fácilmente
	definida como el slice de un array. Usaremos detección de contornos y regiones de interés mucho cuando exploremos los conceptos de detección y seguimiento de objetos.

	Para detectar los contornos de una figura de una imágen utilizamos las funciones cv2.threshold y findContours

	threshold toma como argumentos una imagen fuente, el valor del threshold, el valor máximo y el tipo de threshold y nos devuelve una imágen en la que todos los píxeles
	que no superan el threshold son 0 y todos los que están en el rango adecuado son 255.

	findContours toma como argumentos una imágen fuente, el modo y el método de encontrar los contornos.

	Cuando pasamos el resultado de cv2.threshold a cv2. finCountours podremos encontrar fácilmente los contornos de la imágen. Para dibujarlos utilizamos la función
	cv2.drawContours, que toma como argumentos la imágen destino, los contornos, el índice del contorno a dibujar (negativo para dibujar todos), el color de los contornos
	y otras características del contorno a dibujar (grosor, tipo, etc.) 

	CAJA CONTENEDORA, RECÁNGULA DE ÁREA MÍNIMA, CÍRCULO CONTENEDOR MÍNIMO

	Encontrar los contornos de un cuadrado es simple; las formas irregulares, achatadas y rotadas son las que aprovechan el potencial completo de la función findContours.

	En una aplicación de la vida real nos interesaría determinar la caja contenedora de un sujeto, el recángulo mínimo que lo recubre y el círculo mínimo que lo rodea. La
	función cv2.findContours, en conjunción con otras utilidades de OpenCV, hace de ésta una tarea sencilla. Primero debemos convertir convertir la imagen que leamos a es-
	cala de grises, después aplicamos el threshold y encontramos los contornos de la imagen. Para cada contorno, podemos encontrar y dibujar la caja contenedora, el rectán-
	gulo de área mínima y el círculo de contenedor mínimo. Finalmente, dibujamos los contornos sobre la imágen a color y la mostrarmos.

Día Lunes 2 de Octubre de 2023

	CONTORNOS CONVEXOS Y EL ALGORITMO DOUGLAS-PEUKER

	Cuando trabajamos con contornos, nos podemos encontrar objetos con diversas formas, incluyendo formas convexas. Una forma convexa es aquella en la que no hay dos puntos
	en la figura a los cuales los une una línea que pase por fuera del perímetro de ésta.

	La primera facilidad que nos ofrece OpenCV para calcular una aproximación de un polígono contenedor de una figura es con la función cv2.approxPolyDP. Ésta función toma 
	tres parámetros:
		·Un contorno
		·Un valor épsilon que representa la máxima discrepancia entre el contorno original y el polígono aproximado (A menor valor, más se parecerá el polígono al contorno)
		·Un boolean que indica si el polígono es o no cerrado.

	El valor epsilon es de vital importancia para obtener un contorno útil, por eso debemos entender qué representa exactamente épsilon. Épsilon es la diferencia máxima de
	perímetro que debe de haber entre el contorno original y la aproximación del polígono. Calcular el polígono aproximado es útil a nivel de computación porque representa
	el contorno como un conjunto de rectas.

	Podemos definir epsilon según el perímetro del contorno original gracias a la función cv2.arcLength que toma como parámetros el contorno y un flag booleano.

	OpenCV también ofrece la función cv2.convexHull para obtener información de contorno procesada para figuras convexas.
