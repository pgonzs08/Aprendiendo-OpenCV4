import cv2
# Para capturar frames de la camara debemos pasar el índice de dispositivo
# de la cámara a VideoCapture y podremos leer igual que de un archivo de video

cameraCapture = cv2.VideoCapture(0)
fps = 30 #Asumimos que el video está capturado en este framerate
# El método get de video Capture no es confiable para conseguir framerate de 
# Cámaras. Los frames también pueden tener dimensiones instables al principio de las grabaciones.
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('CameraOutputVid.mov', cv2.VideoWriter_fourcc(*"mp4v"), fps, size)

success = True
nFramesRemaining = 10 * fps #10 seconds of frames
while success and nFramesRemaining > 0:
        #Si no hay frames se devuelve (False, None)
        success, frame = cameraCapture.read()
        videoWriter.write(frame)
        nFramesRemaining -=1

#Cuando queramos sincronizar cámaras usaremos el método grab para comprobar si hay
#fames que leer
