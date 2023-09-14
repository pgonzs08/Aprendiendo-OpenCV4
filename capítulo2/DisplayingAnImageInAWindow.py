import cv2
import numpy as np
import sys

img = cv2.imread(sys.argv[1])
# La funcion imshow muestra un imagen en una ventana con un titulo
cv2.imshow(sys.argv[1], img)
# La ventana no se mostrará hasta que se llame a otra función.
# Al invocar la función waitKey se retorna el keycode de cualquier
# tecla que pulse el usuario en un periodo especificado, si no se pasa
# argmuento devuelve la primera tecla que pulse el usuario
cv2.waitKey()
# destroyAllWindows cierra todas las ventanas creadas por opencv
cv2.destroyAllWindows()