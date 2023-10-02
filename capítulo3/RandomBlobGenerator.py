import cv2
import numpy as np
import random

def generate_blob():
    img = np.zeros((1000, 1000, 3), np.uint8)

    random.seed()

    #Genera aleatoriamente el número de curvas que componen la imágen
    n_circles = random.randint(5, 25)
    print("Generated circles: ", n_circles)

    #Genera las cónicas en los puntos (x,y) seleccionados aleatoriamente con parámetos A, B y r  aleatorios.
    circles = []
    for i in range(n_circles):
        r = random.randint(25, 400)
        circles.append(((random.randint(150, 850), random.randint(150, 850)),random.randint(1, 10), random.randint(1, 10), r, random.randint(0, r//5)))

    # Dibuja los círculos con grosores aleatorios
    for i in range(0, 1000):
        for j in range(0, 1000):
            for point, A, B, r, thickness in circles:

                if A*(i-point[0])**2+B*(j-point[1])**2 <= (r+thickness)**2 and A*(i-point[0])**2+B*(j-point[1])**2 >= (r-thickness)**2:
                    img[i,j] = [255, 255, 255]
                    break

    cv2.imwrite("blob.png", img)

