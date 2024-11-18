import cv2
import numpy as np

video = cv2.VideoCapture('object_video.mp4')

batasbawah_merah1 = (0, 120, 70)
batasatas_merah1 = (10, 255, 255)
batasbawah_merah2 = (170, 120, 70)
batasatas_merah2 = (180, 255, 255)

while video.isOpened():
    read, frame = video.read()
    if not read:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask1 = cv2.inRange(frame_hsv, batasbawah_merah1, batasatas_merah1)
    mask2 = cv2.inRange(frame_hsv, batasbawah_merah2, batasatas_merah2)
    mask = mask1 | mask2

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        luas = cv2.contourArea(contour)
        if luas > 500: 
            x, y, l, t = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + l, y + t), (0, 0, 0), 2)
            cv2.putText(frame, 'Lingkaran Merah', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    cv2.imshow('Deteksi Lingkaran Merah', frame)
    if cv2.waitKey(1) & 0xFF == 13:
        break

video.release()
cv2.destroyAllWindows()
