import cv2
import logging
import time
from parking_management import ParkingManagement


# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
video = cv2.VideoCapture("src-video.mp4")

 # Инициализация объекта управления парковкой
parking_manager = ParkingManagement(
    model="yolo11n.pt",  # путь к файлу модели
    json_file="bounding_boxes.json",  # путь к файлу аннотаций парковки
    )


def main():
       
    try:
        # Открываем RTSP-поток или видеофайл
        cap = video
        
        if not cap.isOpened():
            logging.error("Error opening video stream or file")
            return
        
        # Получаем ширину и высоту кадра
        w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # Переменная для хранения времени последней обработки кадра
        last_processed_time = time.time()
        retry_count = 0  # Счетчик попыток чтения кадра
        max_retries = 5  # Максимальное количество попыток


        while True:
            ret, frame = cap.read()
            if not ret:
                logging.error("Error reading frame from video stream")
                retry_count += 1
                if retry_count >= max_retries:
                    logging.error("Max retries reached. Attempting to reopen the video stream.")
                    cap.release()  # Освобождаем текущий поток
                    cap = video  # Пытаемся снова открыть поток
                    if not cap.isOpened():
                        logging.error("Error reopening video stream or file")
                        break
                    retry_count = 0  # Сбрасываем счетчик попыток
                cv2.waitKey(500) 
                continue

            # Получаем текущее время
            current_time = time.time()

            # Обрабатываем кадр только если прошло время с последней обработки
            if current_time - last_processed_time >= 0.2:
                try:
                    # Обработка кадра с помощью Ultralytics
                    #frame = parking_manager.model.track(frame, persist=True, show=True)
                    frame = parking_manager.process_data(frame)
                    imS = cv2.resize(frame, (w//2, h//2))                # Resize image                    
                    cv2.imshow("output", imS)                       # Show image
                    cv2.waitKey(1) 

                    # Обновляем время последней обработки
                    last_processed_time = current_time
                except Exception as e:
                    logging.error("Error processing frame: %s", e)
                    continue

            # Проверка нажатия клавиш
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                logging.info("User pressed 'q' to quit")
                break

    except Exception as e:
        logging.error("An error occurred: %s", e)
    finally:
        # Освобождение ресурсов
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()