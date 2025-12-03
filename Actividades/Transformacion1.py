import cv2 as cv
import numpy as np
import math

# Cargar la imagen en escala de grises
img = cv.imread('ejemplo1.jpeg', 0)

# Tamaño de la imagen original
x, y = img.shape

# Crear una imagen más grande para la rotación
rotated_img = np.zeros((x*2, y*2), dtype=np.uint8)
xx, yy = rotated_img.shape

# Centro de la imagen original
cx, cy = x // 2, y // 2

# Centro de la imagen destino
ncx, ncy = xx // 2, yy // 2

# Ángulo en radianes
angle = 60
theta = math.radians(angle)

# Rotación centrada
for i in range(x):
    for j in range(y):
        # Coordenadas respecto al centro original
        dx, dy = i - cx, j - cy

        # Aplicar rotación
        new_x = int(dx * math.cos(theta) + dy * math.sin(theta))
        new_y = int(-dx * math.sin(theta) + dy * math.cos(theta))

        # Trasladar al centro de la nueva imagen
        final_x = new_x + ncx
        final_y = new_y + ncy

        if 0 <= final_x < yy and 0 <= final_y < xx:
            rotated_img[final_x, final_y] = img[i, j]

# Mostrar imágenes
cv.imshow('Imagen Original', img)
cv.imshow('Imagen Rotada Centrada', rotated_img)
cv.waitKey(0)
cv.destroyAllWindows()
