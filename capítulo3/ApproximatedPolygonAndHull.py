import cv2
import numpy as np

from RandomBlobGenerator import generate_blob

import sys

if len(sys.argv) == 1:
    generate_blob()
    name = "blob.png"
else:
    name = sys.argv[1]

img = cv2.pyrDown(cv2.imread(name, cv2.IMREAD_UNCHANGED))

ret, thresh = cv2.threshold(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

black = np.zeros_like(img)
for c in contours:
    epsilon = 0.01 * cv2.arcLength(c, True) # 1% discrepacy tolerance
    approx = cv2.approxPolyDP(c, epsilon, True)
    hull = cv2.convexHull(c)
    cv2.drawContours(black, [c], -1, (0,255, 0), 2)
    cv2.drawContours(black, [approx], -1, (255, 255, 0), 2)
    cv2.drawContours(black, [hull], -1, (0, 0, 255), 2)

cv2.imshow("approxpoly_"+name, black)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite("approxpoly"+name, black)