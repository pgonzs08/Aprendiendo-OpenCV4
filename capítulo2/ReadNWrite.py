import numpy as np
import cv2

#En OpenCV y NumPy las imágenes se representan como arrays multidimensionales

img = np.zeros((3,3), dtype=np.uint8)
print(img)
print("Ésta es la representación de un cuadrado negro de 3x3 píxeles en escala de grises")

#En este caso img es un cuadrado negro de 3x3 píxeles, al ser un unsigned int de 8 bits su rango es de 0 a 255
#en opencv éste array representará una imágen en escala de grises donde los valores 0 serán píxeles negros y los valores 255 serán blancos
#y los valores entre éstos dos serán grises de más oscuro a más claro.

print("Con la función cvtColor modificamos la forma y la interpretación de éste array")

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img)
print("Ésta es la representación de un cuadrado negro de 3x3 píxeles en BGR")

#Al utilizar la función cvtColor realmente estamos modificando el array de forma que ahora tenga
#3 valores de 0 a 255 para cada pixel (la forma del array ha pasado de ser (3,3) a (3, 3, 3)) en la tercera dimensión
#del array el índice 0 representa el azul, el 1 el verde y el 2 el rojo (Blue-Green-Red)
#otras formas de representación comunes son el HSV, donde el rango de los valores pasa a ser 0-180
#La forma del array se interpreta, por tanto como (altura, hanchura, canales), si es que hay canales

#Podemos leer imágenes con la función imread. Ésta representa la imágen en BGR por defecto

image = cv2.imread("Foto_CV.JPG")

#Al igual que podemos leer imágenes podemos crear nuevos archivos de imágen con imwrite

cv2.imwrite("Foto_CV.png", image)

#Podemos cambiar el modo de lectura de imread con distintas opciones

image = cv2.imread("Foto_CV.JPG", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("Foto_CV_grayscale.png", image)

image = cv2.imread("Foto_CV.JPG", cv2.IMREAD_ANYCOLOR) #usa el metadata de la imágen para detectar la escala
cv2.imwrite("Foto_CV_anycolor.png", image)

image = cv2.imread("Foto_CV.JPG", cv2.IMREAD_UNCHANGED) #lee todos los datos de la imagen, incluyendo la transparencia como un cuarto canal si la hay
cv2.imwrite("Foto_CV_unchanged.png", image)

image = cv2.imread("Foto_CV.JPG", cv2.IMREAD_ANYDEPTH) #carga la imagen como una en grayscale con un array de ints de 16 bits que representa la profundidad
cv2.imwrite("Foto_CV_anydepth.png", image)