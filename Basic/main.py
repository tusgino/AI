import cv2

import time

## Đọc ảnh
# image = cv2.imread("01.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("Image", image)
#


## Đọc video
id_camera = 1
videoName = "Sample/Video.mp4"

# Mở camera
# video = cv2.VideoCapture(id_camera)

# Mở video
video = cv2.VideoCapture(videoName)

# Convert fps to ms
# 1s = 1000ms
# 1s / 60fps = 1000ms / 60fps
waitTime = 1000 / 60

delay = 1 / 60  # 60fps

while True:
    # Khởi tạo time
    start_time = time.time()

    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    # Cách 2:
    elapsed_time = time.time() - start_time
    sleep_time = delay - elapsed_time

    if sleep_time > 0:
        time.sleep(sleep_time)

    # Cách 1:
    # Đợi 1 phím bấm tương đương với 1 frame
    # key = cv2.waitKey(int(waitTime))

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Giải phóng camera
video.release()

# Dừng mản hình
# cv2.waitKey(0)
cv2.destroyAllWindows()
