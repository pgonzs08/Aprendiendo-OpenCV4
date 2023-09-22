import cv2
from managers import WindowManager, CaptureManager
import filters

"""
    Nuestra aplicaciones es representada por la clase Cameo con dos métodos:
    run y onKeypress. Al inicializar, un objeto Cameo crea un WindowManager
    con onKeypress como callback y un CaptureManager usando una cámara espe-
    cíficamente un cv2.VideoCapture y el mismo WindowManager. Cuando llamamos
    a run la aplicación ejecuta el bucle principal en el que los frames y los
    eventos se procesan
"""
class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
        self._embossFilter = filters.EmbossFilter()
        self._sharpenFilter = filters.SharpenFilter()

    def run(self):
        """Correr el bucle principal"""
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                filters.strokeEdges(frame, frame)
                self._embossFilter.apply(frame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """Manejar pulsaciones de tecla
            espacio -> screenshot
            tab -> empezar/parar grabación
            escape -> salir
        """
        if keycode == 32: #espacio
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9: #tab
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('Screencast.mov')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27: #Escape
            self._windowManager.destroyWindow()


if __name__ == "__main__":
    Cameo().run()
