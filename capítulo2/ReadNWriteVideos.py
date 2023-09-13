import numpy as np
import cv2

# OpenCV proporciona las clases VideoCapture y VideoWriter para la lectura
# y escritura de archivos de video. Los formatos soportados varían según el OS
# y la build de opencv, pero normalmente el formato avi está soportado.
 
bonfire_vid = cv2.VideoCapture("hoguera.mov")

#La funcion get de VideoCapture nos permite obtener propiedades del video leído

fps = bonfire_vid.get(cv2.CAP_PROP_FPS)
size = (int(bonfire_vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(bonfire_vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# Para instanciar un objeto VideoWriter debemos especificar el nombre del archivo
# de output, el codec y además los fps y tamaño del video. El codec 0 da video sin
# comprimir al que debe otorgársele formato avi

output_vid = cv2.VideoWriter("output_vid.mov", cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

# El método read de VideoCapture permite captar frames del video hasta llegar al
# final del archivo, con un loop se pueden obtener todos los frames del video

success = True
frames = []
while success:
    success, frame = bonfire_vid.read()
    frames.append(frame)

for frame in frames:
    output_vid.write(frame)
