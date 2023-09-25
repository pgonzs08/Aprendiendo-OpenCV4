import cv2
import numpy as np

img = cv2.imread("La_verdadera_y_única_Reina_de_España.jpeg", 0)
cv2.imwrite("cala_canny.jpg", cv2.Canny(img, 30, 75))
cv2.imshow("cala canny", cv2.imread("cala_canny.jpg"))
cv2.waitKey()
cv2.destroyAllWindows()