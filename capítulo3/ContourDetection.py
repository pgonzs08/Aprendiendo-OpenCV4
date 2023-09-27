import cv2
import numpy as np

#Crea un cuadrado negro
img = np.zeros((200, 200), dtype=np.uint8)
#Crea un cuadrado blanco dentro del cuadrado negro
img[50:150,50:150] = 255
img[75:125,75:125] = 175

#Detecta las zonas de interés
ret, thresh = cv2.threshold(img, 127, 255, 0)
#Encuentra los contornos de las zonas de interés
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color, contours, -1, (0,255,0), 2)
cv2.imshow("threshold", thresh)
cv2.imshow("Contornos",img)
cv2.waitKey()
cv2.destroyAllWindows()