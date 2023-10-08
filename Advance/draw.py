import time

import cv2
import numpy as np


video = cv2.VideoCapture('Video.mp4')


delay = 1/60
while True:
    start_time = time.time()

    ret, frame = video.read()

    # Lấy chiều rộng và chiều cao của video
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    if not ret:
        break

    # Vẽ đường chéo
    cv2.line(frame, (0,0), (width,height), (255,0,0), 2)

    # Vẽ hình chữ nhật
    cv2.rectangle(frame, (100,100), (200,200), (0,255,0), 2)

    # Vẽ hình tròn
    cv2.circle(frame, (300,300), 100, (0,0,255), 2)

    # Vẽ hình ellipse
    cv2.ellipse(frame, (400,400), (100,50), 0, 0, 180, (255,255,0), 2)

    # Vẽ đa giác
    points = np.array([[500,500], [600,500], [600,600]], np.int32)


    cv2.polylines(frame, [points], True, (0,255,255), 2)

    # Vẽ đa giác fulfilled
    # Chuyển đổi chiều dài của mảng points
    # (-1,1,2) => tuple mô tả hình dáng của mảng
    # -1 => số hàng không xác định (tự động tính toán)
    # 1 => Mỗi điểm là 1 mảng con 1 chiều
    # 2 => Mỗi điểm có 2 giá trị (x, y)
    points_fulfilled = points.reshape((-1, 1, 2))
    cv2.fillPoly(frame, [points_fulfilled], (0,255,255))

    # Vẽ văn bản
    cv2.putText(frame, "Hello", (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2)


    cv2.imshow('Video', frame)

    elapsed_time = time.time() - start_time

    sleep_time = delay - elapsed_time

    if sleep_time > 0:
        time.sleep(sleep_time)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()