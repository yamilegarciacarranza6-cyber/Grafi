import cv2 as cv
import numpy as np
import math

img = cv.imread('ejemplo1.jpeg', 0)
x, y = img.shape

scale_x, scale_y = 2, 2
scaled = np.zeros((x * scale_y, y * scale_x), dtype=np.uint8)

for i in range(x):
    for j in range(y):
        scaled[i * 2, j * 2] = img[i, j]

rows, cols = scaled.shape
for i in range(rows):
    for j in range(cols):
        if scaled[i, j] == 0:
            vecinos = []
            for a in range(-1, 2):
                for b in range(-1, 2):
                    ni, nj = i + a, j + b
                    if 0 <= ni < rows and 0 <= nj < cols and scaled[ni, nj] != 0:
                        vecinos.append(scaled[ni, nj])
            if vecinos:
                scaled[i, j] = int(sum(vecinos) / len(vecinos))

angle = math.radians(45)
cos_a, sin_a = math.cos(angle), math.sin(angle)
h, w = scaled.shape
cx, cy = w // 2, h // 2

rotated = np.zeros_like(scaled)
for i in range(h):
    for j in range(w):
        x0 = int((j - cx) * cos_a + (i - cy) * sin_a + cx)
        y0 = int(-(j - cx) * sin_a + (i - cy) * cos_a + cy)
        if 0 <= y0 < h and 0 <= x0 < w:
            rotated[i, j] = scaled[y0, x0]

cv.imshow('Original', img)
cv.imshow('Escalada + Rotada (bilineal)', rotated)
cv.waitKey(0)
cv.destroyAllWindows()





