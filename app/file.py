import cv2
import sys

image_path = 'image.png'
image = cv2.imread(image_path)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

if len(faces) > 0:
    print(f'Найдено {len(faces)} лицо(а).')
else:
    print('Лица не найдены.')