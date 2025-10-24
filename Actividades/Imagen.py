import cv2 as cv

img = cv.imread("ejemplo1.jpeg")
cv.imshow('Ejemplo', img)
cv.waitKey()
cv.destroyAllWindows