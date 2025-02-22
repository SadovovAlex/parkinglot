# parkinglot
Детектор свободных парковочных мест с использованием Yolo

# Demo
[![Demo Video](https://img.youtube.com/vi/KzB6Gb/default.jpg)](https://github.com/SadovovAlex/parkinglot/raw/main/video1.mp4)
<video width="640" height="480" controls>
  <source src="https://github.com/SadovovAlex/parkinglot/raw/main/video1.mp4" type="video/mp4">
  Ваш браузер не поддерживает встроенные видео.
</video>

#Prerequest
Install cv2 and ultralytics
pip install opencv-python ultralytics

Windows
Microsoft Visual C++ Redistributable is not installed, this may lead to the DLL load failure.
It can be downloaded at https://aka.ms/vs/16/release/vc_redist.x64.exe

#Install
pip install -r requirements.txt

#Run
python ParkingFreeLot.py

После запуска автоматически скачается модель
python ParkingFreeLot.py
Ultralytics Solutions: ✅ {'region': None, 'show_in': True, 'show_out': True, 'colormap': None, 'up_angle': 145.0, 'down_angle': 90, 'kpts': [6, 8, 10], 'analytics_type': 'line', 'json_file': 'bounding_boxes.json', 'records': 5, 'model': 'yolo11n.pt'}
Downloading https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n.pt to 'yolo11n.pt'...
100%|█████████████████████████████████████████████████████████████████████████████| 5.35M/5.35M [00:00<00:00, 10.7MB/s]

#Координаты объектов bounding_boxes.json
 {
        "points": [
            [
                1392,
                839
            ],
            [
                542,
                704
            ],
            [
                402,
                1053
            ],
            [
                1366,
                1069
            ]
        ]
    },

