import cv2
import numpy as np
import os
#podemos castear un a imágen de 8 bits por canal a un bytearray y viceversa

image = cv2.imread("Foto_CV.JPG")
byteArray = bytearray(image)

# Ahora crearemos usando os.urandom

randomByteArray = bytearray(os.urandom(120000))
npByteArray = np.array(randomByteArray)

#Casteamos el array a una imágen cambiando sus dimensiones

grayImage = npByteArray.reshape(300, 400)
cv2.imwrite("GrayNoise.jpg", grayImage)

colorImage = npByteArray.reshape(100, 400, 3)
cv2.imwrite("ColorNoise.jpg", colorImage)

