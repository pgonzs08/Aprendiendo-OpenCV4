import cv2
import numpy as np
import time
"""
    La clase CaptureManager se instancia con un objeto VideoCapture y tiene los
    métodos enterFrame y exitFrame a los que se debe llama en cada ciclo princi-
    pal de la aplicación.

    Entre las invocaciones de enterFrmae y exitFrame se podrá asignart la pro-
    piedad channel y obtener la propiedad frame. Channel es inicialmente 0 y só-
    lo cámaras multihead utilizan otros valores. La propiedad frame is una ima-
    gen correspondiente al estado del canal cuando enterFrame fue llamado.

    La clase CaptureManager también tiene los métodos writeImage, startWriting-
    Video y stopWritingVideo que pueden ser invocados en cualquier momento. La
    escritura de archivos no se realizará hasta invocar exitFrame. Durante el
    método extiFrame, frame puede ser mostrada tanto como argumento al construc-
    tor del CaptureManager como asignando la propiedad previewWindowManager.

    El código de la aplicación mnipula frame, las maniuplaciones son reflejadas
    en archivos grabados y en la ventana. Una clase CaptureManager tiene un argu-
    mento del constructor y una propiedad llamada shouldMirrorPreview que debería
    ser True si queremos que frame se muestre horizontalmente invertido en la ven-
    tana pero no en los archivos grabados. Normalmente los usuarios prefieren que
    al estar enfrentados a la cámara la imágen en vivo esté invertida como si fue-
    se un espejo.

    Como VideoWriter necesita un framerate y opencv no provee un método fiable de
    obtener éste de la cámara la clase CaptureManager se encargará de registrarlo
    con un contador de frames y la función estándar de Python time.time para es-
    timar si es necesario. Dependiendo de las fluctuaciones de framerate y la im-
    plementación dependiente del sistema de time.time, la precisión de la estima-
    ción puede ser pobre. Sin embargo, si mandamos la aplicación en hardware des-
    conocido, es mejor asumir que la cámara del usuario tiene un framerate parti-
    cular-
"""
class CaptureManager(object):
    def __init__(self, capture, previewWindowManager = None, shouldMirrorPreview = False):
        
        # Variables públicas
        self.previewWindowManager = previewWindowManager
        self.shouldMirrorPreview = shouldMirrorPreview
        
        # Variables protegidas
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imageFilename = None
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None
        self._startTime = None
        self._framesElapsed = 0
        self._fpsEstimate = None

    @property
    def channel(self):
        return self._channel
    
    @channel.setter
    def channer(self, value):
        if self._channel != value:
            self._channel = value
            self._frame = None
        
    @property
    def frame(self):
        if self._enteredFrame and self._frame is None:
            _, self._frame = self._capture.retrieve(self._frame, self._channel)
        return self._frame
    
    @property
    def isWritingImage(self):
        return self._imageFilename is not None
    
    @property
    def isWritingVideo(self):
        return self._videoFilename is not None
    
    def enterFrame(self):
        """Capturar el próximo frame, si lo hay."""
        # Primero comprobamos que el último frame fue expulsado
        assert not self._enteredFrame, 'en anterior enterFrame() no tuve exitFrame() correspondiente'
        if self._capture is not None:
            self._enteredFrame = self._capture.grab()

    def exitFrame(self):
        """Dibuja a la ventana. Escribe a los archvios. Libera el frame."""

        #Comprueba is le frame agarrado puede ser devuelto.
        #El getter puede devolver y cachear el frame.

        if self.frame is None:
            self._enteredFrame = False
            return
        
        if self._framesElapsed == 0:
            self._startTime = time.time()
        else:
            timeElapsed = time.time() - self._startTime
            self._fpsEstimate = self._framesElapsed / timeElapsed
            self._framesElapsed += 1

        #Dibujar en la ventana, si hay
        if self.previewWindowManager is not None:
            if self.shouldMirrorPreview:
                mirroredFrame = np.fliplr(self._frame)
                self.previewWindowManager.show(mirroredFrame)
            else:
                self.previewWindowManager.show(self._frame)

        #Escribir en el archivo de image, si hay
        if self.isWritingImage:
            cv2.imwrite(self._imageFilename, self._frame)
            self._imageFilename = None

        #Escribir en el archivo de video, si hay
        self._writeVideoFrame()

        #Liberar el frame
        self._frame = None
        self._enteredFrame = False

    def writeImage(self, filename):
        """Escribe el sigueinte frame expulsado en un archivo de imagen"""
        self._imageFilename = filename

    def startWritingVideo(self, filename, encoding=cv2.VideoWriter_fourcc(*'mp4v')):
        """Empieza a escribir frames expulsados en un archivo de video"""
        self._videoFilename = filename
        self._videoEncoding = encoding

    def stopWritingVideo(self):
        """Deja de escribir frames expulsados en un archvio de video"""
        self._videoFilename = None
        self._videoEncoding = None
        self._videoWriter = None

    def _writeVideoFrame(self):
        if not self.isWritingVideo:
            return
        if self._videoWriter is None:
            fps = self._capture.get(cv2.CAP_PROP_FPS)
            if fps <= 0.0:
                #Los fps de captura son desconocidos así que usamos estimado
                if self._framesElapsed < 20:
                    # Esperamos hasta que pasen más frames para que el estimado sea estable
                    return
                else:
                    fps = self._fpsEstimate
            size = (int(self._capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self._capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            self._videoWriter = cv2.VideoWriter(self._videoFilename, self._videoEncoding, fps, size)
        self._videoWriter.write(self._frame)


class WindowManager(object):
    def __init__(self, windowName, keypressCallback=None):
        self.keypressCallback = keypressCallback
        self._windowName = windowName
        self._isWindowCreated = False
    
    @property
    def isWindowCreated(self):
        return self._isWindowCreated
    
    def createWindow(self):
        cv2.namedWindow(self._windowName)
        self._isWindowCreated = True
    
    def show(self, frame):
        cv2.imshow(self._windowName, frame)
    def destroyWindow(self):
        cv2.destroyWindow(self._windowName)
        self._isWindowCreated = False
    def processEvents(self):
        keycode = cv2.waitKey(1)
        if self.keypressCallback is not None and keycode != -1:
            self.keypressCallback(keycode)