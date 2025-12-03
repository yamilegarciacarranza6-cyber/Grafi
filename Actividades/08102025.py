
import cv2 as cv
import math  
               
rostro = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)

frame_count = 0  

while True:
    ret, img = cap.read()
    gris = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rostros = rostro.detectMultiScale(gris, 1.3, 5)

    
    frame_count += 1
    eye_move = int(3 * math.sin(frame_count * 0.2))       
    tongue_move = int(5 * abs(math.sin(frame_count * 0.3)))  
    for (x, y, w, h) in rostros:
        res = int((w + h) / 8)
        img = cv.rectangle(img, (x, y), (x + w, y + h), (234, 23, 23), 5)
        img = cv.rectangle(img, (x, int(y + h / 2)), (x + w, y + h), (0, 255, 0), 5)

      
        img = cv.circle(img, (x + int(w * 0.3), y + int(h * 0.4)), 21, (0, 0, 0), 2)
        img = cv.circle(img, (x + int(w * 0.7), y + int(h * 0.4)), 21, (0, 0, 0), 2)
        img = cv.circle(img, (x + int(w * 0.3), y + int(h * 0.4)), 20, (255, 255, 255), -1)
        img = cv.circle(img, (x + int(w * 0.7), y + int(h * 0.4)), 20, (255, 255, 255), -1)
       
        img = cv.circle(img, (x + int(w * 0.3) + eye_move, y + int(h * 0.4)), 5, (0, 0, 255), -1)
        img = cv.circle(img, (x + int(w * 0.7) + eye_move, y + int(h * 0.4)), 5, (0, 0, 255), -1)

       
        mouth_top = y + int(h * 0.75)
        mouth_bottom = y + int(h * 0.9)
        img = cv.rectangle(img, (x + int(w * 0.3), mouth_top),
                           (x + int(w * 0.7), mouth_bottom), (0, 0, 0), -1)

        
        tongue_top = mouth_bottom - 10 + tongue_move
        tongue_bottom = mouth_bottom + 10 + tongue_move
        tongue_center_x = x + int(w * 0.5)
        img = cv.rectangle(img, (tongue_center_x - 10, tongue_top),
                           (tongue_center_x + 10, tongue_bottom), (0, 0, 255), -1)

    cv.imshow('img', img)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()  
cv.destroyAllWindows()
