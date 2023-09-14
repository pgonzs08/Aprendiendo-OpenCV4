import numpy as np
import cv2
import sys

#Gracias a los arrays de numpy podemos realizar operaciones sobre las
#imágenes de opencv que no están disponibles en las listas de python.

#Podemos modificar píxeles concretos y en grupo modificando sus valores en el array de la imágen

image = cv2.imread("Foto_CV.JPG")
image[0,0] = [255,255,255] #Convierte el pixel en la posición 0,0 a blanco

#Las funciones item e itemset permiten el acceso y la modificación de valores únicos en el array

print(f"Modificando el canal 1 del pixel (100, 100) de {image.item(100,100,1)} a ")
image.itemset((100, 100, 1), 122)
print(image.item(100, 100, 1))

cv2.imwrite("Nosenota.png", image)

#Por razones de eficiencia estas funciones se utilizarán para modificaciones pequeñas en regiones de interés
#Cuando necesitemos manipular regiones grandes es mejor utilizar o funciones de opencv o array slicing

image[:,:,1] = 255

cv2.imwrite("Verde.png", image)

image = cv2.imread(sys.argv[1])

right_side = image[:,image.shape[1]//2:,:]
cv2.imwrite("lado_derecho.png", right_side)

#Invertimos horizontalmente la media imagen
inverted_right_side = right_side[:,::-1,:]

#Sustituimos el ojo izquierdo por el derecho
image[:,:image.shape[1]//2,:] = inverted_right_side
cv2.imwrite(sys.argv[2], image)
