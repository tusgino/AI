# OpenCV Hướng dẫn từ cơ bản đến nâng cao

OpenCV (Open Source Computer Vision Library) là một thư viện mã nguồn mở chuyên về xử lý ảnh và xử lý video. Dưới đây là hướng dẫn cài đặt và sử dụng OpenCV.

## Mục lục

1. [Cài đặt](#installation)
2. [Bắt đầu với OpenCV](#getting-started)
3. [Chức năng cơ bản](#basic-functions)

## 1. Cài đặt <a name="installation"></a>

### 1.1 Windows

- **Pip**

```
pip install opencv-python
```

- **Conda**

```
conda install -c conda-forge opencv
```

### 1.2 Linux (Ubuntu/Debian)

- **Pip**

```
pip install opencv-python
```

- **Apt**

```
sudo apt update
sudo apt install python3-opencv
```

### 1.3 macOS

- **Pip**

```
pip install opencv-python
```

- **Homebrew**

```
brew install opencv
```

---

## 2. Bắt đầu với OpenCV <a name="getting-started"></a>

### 2.1 Đọc và hiển thị ảnh

```python
import cv2

# Đọc ảnh (.jpg, .png, ...)
image = cv2.imread('path_to_image.jpg')

# Đọc ảnh dưới dạng ảnh xám
image_gray = cv2.imread('path_to_image.jpg', 0)

#Lưu ảnh
cv2.imwrite('path_to_save_image.jpg', image)

# Hiển thị ảnh
cv2.imshow('Image Title', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

### 2.2 Đọc và hiển thị video

```python
# Mở video
import cv2

# Mở camera
# video = cv2.VideoCapture(id_camera)
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
```

---

## 3. Chức năng cơ bản <a name="basic-functions"></a>

### 3.1 Chuyển đổi màu sắc

#### 3.1.1 Chuyển đổi màu sắc với OpenCV

```python
import cv2


# Đọc ảnh xám
# image = cv2.imread("01.png", cv2.IMREAD_GRAYSCALE)
# cv2.imwrite("01_gray.png", image)

# Đọc ảnh màu
# Ảnh mặc định là hệ màu BGR (Blue, Green, Red)

image = cv2.imread("01.png")
cv2.imshow("Image Color", image)
cv2.waitKey(0)

# Biến đổi ảnh sang xám
# COLOR_BGR2GRAY: Chuyển từ ảnh màu sang xám
# COLOR_GRAY2BGR: Chuyển từ ảnh xám sang màu
# COLOR_BGR2RGB: Chuyển từ ảnh màu sang màu khác
# COLOR_RGB2BGR: Chuyển từ ảnh màu sang màu khác
# COLOR_BGR2HSV: Chuyển từ ảnh màu sang HSV
# COLOR_HSV2BGR: Chuyển từ ảnh HSV sang màu
# COLOR_BGR2YCrCb: Chuyển từ ảnh màu sang YCrCb
# COLOR_YCrCb2BGR: Chuyển từ ảnh YCrCb sang màu
# COLOR_BGR2XYZ: Chuyển từ ảnh màu sang XYZ
# COLOR_XYZ2BGR: Chuyển từ ảnh XYZ sang màu
# COLOR_BGR2Lab: Chuyển từ ảnh màu sang Lab
# COLOR_Lab2BGR: Chuyển từ ảnh Lab sang màu
# ...

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("Image Gray", image_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

#### 3.1.2 Các hệ màu cơ bản

```python
HSV: Hue, Saturation, Value (0,0,0):(360,100,100)
HSL: Hue, Saturation, Lightness (0,0,0):(360,100,100)
RGB: Red, Green, Blue (0,0,0):(255,255,255)
CMYK: Cyan, Magenta, Yellow, Key (Black) (0,0,0,0):(100,100,100,100)
BGR: Blue, Green, Red (0,0,0):(255,255,255)
GRAY: Gray (0):(255)
```

---

### 3.2 Làm mờ ảnh (phần đọc thêm)

Việc làm mờ hình ảnh thường được sử dụng trong xử lý hình ảnh để giảm tiếng ảnh, giúp loại bỏ nhiễu hoặc khi bạn muốn làm mềm chi tiết của một bức ảnh. OpenCV cung cấp nhiều phương pháp để làm mờ ảnh, dưới đây là một số phương pháp phổ biến:

1. **Làm mờ trung bình (Averaging Blur)**: Ở đây, bạn lấy trung bình của tất cả các pixel dưới vùng kernel và thay thế giá trị trung tâm bằng giá trị trung bình đó.

```python
import cv2

image = cv2.imread("path_to_image.jpg")
blurred_image = cv2.blur(image, (5,5))
# (5,5) là kích thước kernel
# Kích thước kernel càng lớn thì ảnh càng mờ
# với 5,5 thì ảnh sẽ được làm mờ với kernel 5x5, có nghĩa là 1 pixel sẽ được làm mờ
# bằng trung bình của 25 pixel xung quanh nó
# Ví dụ, pixel hiện tại có (200,150,100) và tổng giá trị lần lượt các kênh màu R, G, B của 25 pixel xung quanh nó là (1000, 1200, 1500)
# thì pixel hiện tại sẽ được làm mờ thành (1000/25, 1200/25, 1500/25) = (40, 48, 60)

cv2.imshow("Averaging Blur", blurred_image)
cv2.waitKey(0)
```

2. **Làm mờ Gaussian (Gaussian Blur)**: Làm mờ sử dụng kernel Gaussian. Điều này thường hiệu quả hơn khi loại bỏ nhiễu Gaussian.

```python
gaussian_blurred = cv2.GaussianBlur(image, (5,5), 0)
# Làm mờ có cấp độ từ trung tâm ra rìa của kernel
# 0 là mức độ làm mờ
# => Làm cho ảnh có độ mờ mượt hơn
cv2.imshow("Gaussian Blur", gaussian_blurred)
cv2.waitKey(0)
```

3. **Làm mờ trung vị (Median Blur)**: Chỉ thích hợp cho việc loại bỏ nhiễu muối tiêu trên ảnh.

```python
median_blurred = cv2.medianBlur(image, 5)
# Nhận số lẻ làm kích thước kernel
# 5 là kích thước kernel
# Nếu số chẵn thì công thức tính trung vị sẽ không chính xác, dẫn đến lỗi
cv2.imshow("Median Blur", median_blurred)
cv2.waitKey(0)
```

4. **Làm mờ song song (Bilateral Filter)**: Giữ lại cạnh của hình ảnh trong khi làm mờ. Điều này giúp giữ chi tiết trong khi loại bỏ nhiễu.

```python
bilateral_blurred = cv2.bilateralFilter(image, 9, 75, 75)
cv2.imshow("Bilateral Blur", bilateral_blurred)
cv2.waitKey(0)
```

---

### 3.3 Resize ảnh

```python
import cv2

image = cv2.imread("01.png")

# Resize dsize=(width, height)
# Resize tuyệt đối
resized_image = cv2.resize(image, dsize=(200, 200))

# Resize tỉ lệ
resized_image_ratio = cv2.resize(image, dsize=None, fx=0.5, fy=0.5)

# Nội suy inerpolation (thực tế ít dùng vì thực sự khó thấy sự khác biệt)
# INTER_NEAREST: Lấy giá trị điểm ảnh gần nhất
# INTER_LINEAR: Lấy giá trị điểm ảnh trung bình
# INTER_AREA: Lấy giá trị điểm ảnh gần nhất
# INTER_CUBIC: Lấy giá trị điểm ảnh trung bình
# INTER_LANCZOS4: Lấy giá trị điểm ảnh trung bình
resized_image_ratio_inter = cv2.resize(image, dsize=None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Image", image)
cv2.imshow("Resized Image", resized_image)
cv2.imshow("Resized Image Ratio", resized_image_ratio)

cv2.waitKey(0)
cv2.destroyAllWindows()

```

---

### 3.4 Rotate ảnh

**1. Rotate ảnh với OpenCV(Cơ bản)**

```python
import cv2

angle = {
    "0": 0,
    "45": 45,
    "90": 90,
    "180": 180,
    "270": 270
}

scale = 1.0


image = cv2.imread("01.png")
(h, w) = image.shape[:2]
center = (w / 2, h / 2)

# Lấy ma trận (affine) xoay ảnh 45 độ quanh tâm ảnh với tỉ lệ scale = 1.0
M = cv2.getRotationMatrix2D(center, angle["45"], scale)

# Xoay ảnh với ma trận M vừa lấy được ở trên với kích thước ảnh ban đầu
rotated_image = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Image", image)
cv2.imshow("Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

**2. Rotate ảnh với OpenCV(Thư viện imutils)**

```python
import cv2
import imutils
[...] # Tương tự như trên
# Dễ dàng hơn rất nhiều
rotated_image = imutils.rotate(image, angle["45"])
cv2.imshow("Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

### 3.5 Threshold

#### 3.5.1 Thread Binary

- Một bức ảnh màu thông thường sẽ có ba mảng 2 chiều tương ứng với 3 kênh màu RGB. Mỗi mảng 2 chiều chứa giá trị trong khoảng từ 0 đến 255.

- Ảnh xám chỉ chứa một mảng 2 chiều, với mỗi phần tử có giá trị nằm trong khoảng từ 0 đến 255.

- Ảnh nhị phân cũng chỉ bao gồm một mảng 2 chiều, nhưng mỗi phần tử chỉ có giá trị là 0 hoặc 255.

- **Lý do chúng ta cần áp dụng thresholding cho ảnh**:

  - Giúp tách biệt các đối tượng trong ảnh khỏi nền, giúp chúng ta dễ dàng tập trung vào phần quan trọng của ảnh.
  - Nhiều thuật toán thị giác máy tính hoạt động hiệu quả hơn trên ảnh nhị phân so với ảnh xám hay ảnh màu.
  - Dễ dàng phát hiện và theo dõi đối tượng hơn so với khi sử dụng ảnh xám hay ảnh màu.
  - Giảm kích thước ảnh và tiết kiệm không gian lưu trữ.
  - Tạo sơ đồ ảnh (histogram) và loại bỏ thông tin không cần thiết, giúp tập trung vào đặc điểm nổi bật của ảnh.

```python
import cv2

image = cv2.imread("01.png")

# Convert Gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threashold
# THREAD_BINARY: Nếu giá trị pixel > threashold thì pixel đó sẽ được gán giá trị maxval
# THREAD_BINARY_INV: Nếu giá trị pixel > threashold thì pixel đó sẽ được gán giá trị 0
ret, threashold_image = cv2.threshold(image_gray, 127,255, cv2.THRESH_BINARY)

if ret:
    # Nếu convert thành công thì hiển thị ảnh
    cv2.imshow("Image", image)
    cv2.imshow("Image Gray", image_gray)
    cv2.imshow("Threashold Image", threashold_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")
```

=> Nhược điểm: Chúng ta phải tự định nghĩa threashold, nên nếu gặp những bức ảnh có độ tương phản thấp thì sẽ không đạt hiệu quả mong muốn.

#### 3.5.2 Adaptive Threshold

- Để khắc phục nhược điểm của Threshold Binary, chúng ta sử dụng Adaptive Threshold. Đây là một phương pháp tự động xác định threashold cho từng vùng của ảnh.

```python
import cv2

image = cv2.imread("01.png")

# Convert to Gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Adaptive Threshold

# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)
# ADAPTIVE_THRESH_MEAN_C: Giá trị threshold được tính bằng trung bình của các pixel xung quanh
# ADAPTIVE_THRESH_GAUSSIAN_C: Giá trị threshold được tính bằng trung bình có trọng số của các pixel xung quanh
# C: Giá trị thêm vào sau khi tính toán threshold
# blockSize: Kích thước của vùng xung quanh mỗi pixel
# => blockSize càng lớn thì ảnh càng mờ
# Càng nhỏ thì ảnh càng sắc nét

threshold_image = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 4)

if threshold_image is not None:
    # Nếu convert thành công thì hiển thị ảnh
    cv2.imshow("Image", image)
    cv2.imshow("Image Gray", image_gray)
    cv2.imshow("Threshold Image", threshold_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error")
```

Ví dụ:

- Phát hiện biển số xe
- Phát hiện đường
- Phát hiện đối tượng

---
