import cv2
import numpy as np
import utils

"""
    Para la detección de bordes opencv provee múltiples filtros que transforman
    regiones sin borden en negro y regiones con borden en blanco o colores saturados.
    Éstos filtros suelen confundir ruido con bordes, para reducir éste efecto primero
    aplicamos un filtro de desenfoque que elimine las frecuencias más altas.

    Tras filtrar la imágen podemos construir una máscara que multiplicar por la imágen
    para ennegrecer los bordes.
"""

def strokeEdges(src, dst, blurKsize=7,edgeKsize=5):
    # Obtenemos una imagen en blanco y negro adecuada
    if blurKsize >=3:
        # Si el kernel es muy grande difuminamos primero para reducir el ruido
        blurredSrc = cv2.medianBlur(src, blurKsize)
        graySrc = cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src, cv2.cvtColor(cv2.COLOR_BGR2GRAY))
    
    # Aplicamos un filtro de detección de bordes
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize = edgeKsize)

    # Creamos una máscara que conserve los píxeles que no son bordes
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)

    # Multiplicamos cada uno de los canales de color por la máscara y los volvemos a unir
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels, dst)