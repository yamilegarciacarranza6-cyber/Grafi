import cv2 as cv
import numpy as np

# Cargar la imagen en escala de grises
img = cv.imread('ejemplo1.jpeg', 0)
# Obtener el tamaño de la imagen
x, y = img.shape
# Definir el factor de escala
scale_x, scale_y = 2, 2
# Crear una nueva imagen para almacenar el escalado
scaled_img = np.zeros((int(x * scale_y), int(y * scale_x)), dtype=np.uint8)
# Aplicar el escalado
for i in range(x):
    for j in range(y):
                   #orig_x = int(i * scale_y)
                   #orig_y = int(j * scale_x)
                   scaled_img[i*2, j*2] = img[i, j]


rows, cols = scaled_img.shape
for i in range(rows):
    for j in range(cols):
        if scaled_img[i, j] == 0:
            vecinos = []
            for a in range(-1, 2):
                for b in range(-1, 2):
                    ni, nj = i + a, j + b
                    if 0 <= ni < rows and 0 <= nj < cols:
                        val = scaled_img[ni, nj]
                        if val != 0:
                            vecinos.append(val)
            if vecinos:
                scaled_img[i, j] = int(sum(vecinos) / len(vecinos))

                
# Mostrar la imagen original y la escalada
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Escalada (modo raw)', scaled_img)
cv.waitKey(0)
cv.destroyAllWindows()