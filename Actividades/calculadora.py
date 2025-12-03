import cv2
import mediapipe as mp
import numpy as np

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Definir botones de la calculadora
botones = [
    {'label': '1', 'pos': (50, 100)}, {'label': '2', 'pos': (150, 100)}, {'label': '3', 'pos': (250, 100)},
    {'label': '4', 'pos': (50, 200)}, {'label': '5', 'pos': (150, 200)}, {'label': '6', 'pos': (250, 200)},
    {'label': '7', 'pos': (50, 300)}, {'label': '8', 'pos': (150, 300)}, {'label': '9', 'pos': (250, 300)},
    {'label': '0', 'pos': (150, 400)}, {'label': '+', 'pos': (350, 100)}, {'label': '-', 'pos': (350, 200)},
    {'label': '*', 'pos': (350, 300)}, {'label': '/', 'pos': (350, 400)}, {'label': '=', 'pos': (250, 400)},
    {'label': 'C', 'pos': (50, 400)}  # Botón para limpiar
]

operacion = ""
ultimo_click = ""

# Captura de video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Dibujar botones
    for boton in botones:
        x, y = boton['pos']
        cv2.rectangle(frame, (x, y), (x+80, y+80), (200, 200, 200), -1)
        cv2.putText(frame, boton['label'], (x+25, y+50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

    # Procesar mano
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Coordenadas del dedo índice
            x_indice = int(hand_landmarks.landmark[8].x * w)
            y_indice = int(hand_landmarks.landmark[8].y * h)
            cv2.circle(frame, (x_indice, y_indice), 10, (0, 255, 0), -1)

            # Detectar si el dedo está sobre un botón
            for boton in botones:
                x, y = boton['pos']
                if x < x_indice < x+80 and y < y_indice < y+80:
                    if boton['label'] != ultimo_click:
                        if boton['label'] == '=':
                            try:
                                resultado = str(eval(operacion))
                                operacion = resultado
                            except:
                                operacion = "Error"
                        elif boton['label'] == 'C':
                            operacion = ""
                        else:
                            operacion += boton['label']
                        ultimo_click = boton['label']
                    break
            else:
                ultimo_click = ""

    # Mostrar operación actual
    cv2.putText(frame, f"Operacion: {operacion}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2)

    cv2.imshow("Calculadora con MediaPipe", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()