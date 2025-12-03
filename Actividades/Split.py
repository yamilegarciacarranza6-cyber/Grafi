import cv2 as cv
import numpy as np

img= cv.imread('1a.jpeg', 1)

img2= np.zeros((img.shape[:2]), dtype=np.uint8)

print(img.shape[:2])

r, g, b =cv.split(img)

r2= cv.merge([img2, img2, r])
g2= cv.merge([img2, g, img2])
b2= cv.merge([b, img2, img2])
img3= cv.merge([b, r, g])



cv.imshow('ejemplo', img)
cv.imshow('r2', r2)
cv.imshow('g2', g2)
cv.imshow('b2', b2)

# Muestra la imagen que contiene solo el canal rojo.
#cv.imshow('r', r)
#cv.imshow('r2', r2)



# Muestra la imagen que contiene solo el canal verde.
#cv.imshow('g', g)
#cv.imshow('g2', g2)

# Muestra la imagen que contiene solo el canal azul.
#cv.imshow('b', b)
#cv.imshow('b2', b2)



cv.imshow('img3', img3)

# Espera indefinidamente a que el usuario presione una tecla.
cv.waitKey(0)

# Cierra todas las ventanas abiertas por OpenCV.
cv.destroyAllWindows()
