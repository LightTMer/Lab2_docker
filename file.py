import cv2
import sys

# Получаем путь к изображению из аргументов командной строки
if len(sys.argv) == 2:
    image_path = sys.argv[1]

else:
    image_path = "./image.png"



image = cv2.imread(image_path)

# Загружаем каскад для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Преобразуем изображение в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Обнаруживаем лица
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Проверяем, найдены ли лица
if len(faces) > 0:
    print(f'Найдено {len(faces)} лицо(а).')
    
    # Рисуем красные прямоугольники вокруг найденных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Красный цвет (BGR)
    
    # Сохраняем изображение с прямоугольниками
    output_path = 'output_image.jpg'  # Укажите желаемое имя файла
    cv2.imwrite(output_path, image)
    print(f'Изображение сохранено как {output_path}')
    
    # # Отображаем изображение с прямоугольниками
    # cv2.imshow('Faces found', image)
    # cv2.waitKey(0)  # Ждем нажатия клавиши
    # cv2.destroyAllWindows()  # Закрываем все окна
else:
    print('Лица не найдены.')
