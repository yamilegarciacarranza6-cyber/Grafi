import cv2 as cv
import numpy as np
import math

img = cv.imread('ejemplo1.jpeg', 0)
x, y = img.shape

canvas = np.zeros((x * 3, y * 3), dtype=np.uint8)
start_x = x
start_y = y
canvas[start_x:start_x + x, start_y:start_y + y] = img

angle = math.radians(90)
cos_a, sin_a = math.cos(angle), math.sin(angle)
h, w = canvas.shape
cx, cy = w // 2, h // 2

rotated = np.zeros_like(canvas)
for i in range(h):
    for j in range(w):
        x0 = int((j - cx) * cos_a + (i - cy) * sin_a + cx)
        y0 = int(-(j - cx) * sin_a + (i - cy) * cos_a + cy)
        if 0 <= y0 < h and 0 <= x0 < w:
            rotated[i, j] = canvas[y0, x0]

rows, cols = rotated.shape
scaled = np.zeros((rows * 2, cols * 2), dtype=np.uint8)
for i in range(rows):
    for j in range(cols):
        scaled[i * 2, j * 2] = rotated[i, j]

rows2, cols2 = scaled.shape
for i in range(rows2):
    for j in range(cols2):
        if scaled[i, j] == 0:
            vecinos = []
            for a in range(-1, 2):
                for b in range(-1, 2):
                    ni, nj = i + a, j + b
                    if 0 <= ni < rows2 and 0 <= nj < cols2 and scaled[ni, nj] != 0:
                        vecinos.append(scaled[ni, nj])
            if vecinos:
                scaled[i, j] = int(sum(vecinos) / len(vecinos))

cv.imshow('Trasladar + Rotar + Escalar (bilineal)', scaled)
cv.waitKey(0)
cv.destroyAllWindows()
