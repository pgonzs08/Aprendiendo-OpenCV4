import cv2
import numpy as np
from scipy import ndimage

# La operaciones de convolución y correlación son operaciones entre matrices
# que consisten en transformar cada píxel de la matriz con la otra.
# La matriz con la que se realiza la convolución y la correlación es llamada
# kernel y sus características nos dicen qué podemos esperar de la convolución
# de ésta con cualquier matriz a la que para éste tema nos conviene llamar imagen.
# Por ejemplo:

kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])

# Para entender cómo las características de éstos kernel tenemos que entender cómo
# funciona la convolución y la correlación.
# Al realizar las operaciones de convolución y correlación debemos imaginar que el kernel
# Es una ventana que estamos deslizándo por la imagen haciendo coincidir el centro del kernel
# con cada uno de los píxeles de ésta de forma que haya una correspondencia uno a uno entre
# cada píxel del vecindario en el que estamos de la imagen y cada valor del kernel.
# Para operar se multiplica cada valor del kernel por el que corresponde y después se suman 
# los resultados de todos los productos. Tras haber deslizado el kernel por cada píxel de la 
# imagen obtendremos otra imagen cuyos píxeles serán todos los resultados que obtuvimos en sus
# homólogos en la imágen original.
# Ahora que sabemos ésto podemos analizar los kernel anteriores para determinar qué podemos
# esperar de la imagen resultante.
# Un kernel define una señal discreta y al realizar una convolución o correlación aumentamos 
# el valor absoluto de los píxeles de las zonas de las imágenes que sean similares a esa señal 
# mientras que disminuimos los de zonas distintas a esa señal.
# En el caso de los kernel de ejemplo el análisis matemático de la operación nos indica que 
# Aquellas zonas en las que los píxeles del centro sean distintas a sus circundantes tendrán 
# mayor valor absoluto que las que tengan todos los píxeles iguales.
# Si comparamos las transformadas de fourier de la imagen original y la resultado de una convo-
# lución o correlación con uno de éstos kernel podremos observar que la imágen resultado tiene
# menos sinusoides de baja frecuencia que la original, por lo que al ver éste kernel sabemos que
# es High Pass.

img = cv2.imread("La_verdadera_y_única_Reina_de_España.jpeg", 0)

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = (cv2.GaussianBlur(img,(17,17), 0))
g_hpf = img - blurred

cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("blurred", blurred)
cv2.imshow("h_hpf", g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()

# La diferencia entre correlación y convolución es que la convolución se hace con el kernel
# traspuesto, por tanto en kernels simétricos podemos hablar indistíntamente de ellas, pero en 1d
# la cosa cambia.

# Una de las ventajas de la convolución es que no tiene por qué ser necesariamente
# con kernel bidimensionales, por ejemplo:
k_1d = np.array([1/6,2/3,1/6], np.float32)# es un kernel 1d low-pass

# Hacer la correlación y la convolución seguidas de éste mismo kernel es lo mismo que hacer una sola
# de el cuadrado de ese kernel:

k_2d = np.atleast_2d(k_1d).T @ np.atleast_2d(k_1d)
print(k_2d)

k_1d_img = cv2.sepFilter2D(img, 0, k_1d, k_1d)
k_2d_img = ndimage.convolve(img, k_2d)

cv2.imshow("2 1d", k_1d_img)
cv2.imshow("1 2d", k_2d_img)
cv2.waitKey()
cv2.destroyAllWindows()