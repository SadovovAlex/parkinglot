from parking_management import ParkingPtsSelection
import cv2

video = cv2.VideoCapture("src-video.mp4")

 # Проверяем, удалось ли открыть видеопоток
if not video.isOpened():
    print("Ошибка: Не удалось открыть видеопоток.")
else:
    # Читаем один кадр
    ret, frame = video.read()
     
    if ret:
        # Сохраняем кадр как изображение
        cv2.imwrite("screenshot.png", frame)
        print("Скриншот сохранен как screenshot.png")
    else:
        print("Ошибка: Не удалось прочитать кадр.")

# запускаем UI регионов
ParkingPtsSelection()