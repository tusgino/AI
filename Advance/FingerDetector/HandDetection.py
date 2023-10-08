import os
import cv2
import time
import numpy as np

import hand_lib as handLib


video = cv2.VideoCapture(1)

pathFolder = "Fingers"

list = os.listdir(pathFolder)
list.sort()

listImage = []

for file in list:
    # Đọc ảnh giữ nguyên kênh màu
    # image = cv2.imread(pathFolder + "/" + file, cv2.IMREAD_UNCHANGED)
    image = cv2.imread(pathFolder + "/" + file)
    # print(pathFolder + "/" + file)
    listImage.append(image)

print(listImage[0].shape)

start_time = 0

detector = handLib.handDetector()

while True:
    ret, frame = video.read()


    frame, hand_lms = detector.findHands(frame)

    index = detector.count_finger(hand_lms)

    if not ret:
        break

    imageHand = listImage[index]

    h, w, c = imageHand.shape

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))

    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

    frame[0:h, 0:w] = imageHand

    end_time = time.time()

    fps = 1/(end_time - start_time)

    start_time = end_time

    # fps sẽ có kiểu float, nên cần chuyển về kiểu int
    cv2.putText(frame, "FPS: "+ str(int(fps)), (width-200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Hand Detection', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break