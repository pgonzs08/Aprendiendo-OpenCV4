import cv2

clicked = False

#Handler para el evento click del ratón
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        #indica a través de la variable global que se ha hecho clicm
        clicked = True

#Capturador de cámara
cameraCapture = cv2.VideoCapture(0)
#Nombramos la venta que vamos a utilizar y asignamos el handler del evento click del ratón
cv2.namedWindow('ElOjoDelPortatil')
cv2.setMouseCallback('ELOjoDelPortatil', onMouse)

print("Mostrando vista de cámara. Haz click en la ventan o pulsa a cualquier tecla para parar")
success = True

#Mostramos los frames capturados en la ventana hasta que el usuario pulse una tecla o hagamos click en la ventana
while success and cv2.waitKey(1) == -1 and not clicked:
    success, frame = cameraCapture.read()
    cv2.imshow('ElOjoDelPortatil', frame)

#Cerramos la ventana
cv2.destroyWindow('ElOjoDelPortatil')
cameraCapture.release()