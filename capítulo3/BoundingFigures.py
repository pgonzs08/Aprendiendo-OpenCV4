import numpy as np
import cv2
import sys

from RandomBlobGenerator import generate_blob


#Generates a random complex image made from conics
if len(sys.argv) == 1:
    generate_blob()
    name = "blob.png"
else:
    name = sys.argv[1]

img = cv2.imread(name, cv2.IMREAD_UNCHANGED)

img = cv2.pyrDown(img)

ret, thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    #find bounding box coordinates
    x, y, w ,h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

    #find minimum area
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    #normalize coordinates to integers
    box = np.int0(box)
    #draw contours
    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)

    #calculate center and radius of minimum enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    # cast to int
    center = (int(x), int(y))
    radius = int(radius)
    #draw the circle
    img = cv2.circle(img, center, radius, (0, 255, 255), 2)

cv2.drawContours(img, contours, -1, (0, 255, 0), 2)


cv2.imshow("Blobby, contours and bounding figures", img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("bound_"+name, img)