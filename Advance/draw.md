# Vẽ hình trên ảnh với openCV

## Mục lục

1. [Vẽ đường thẳng](#line)
2. [Vẽ hình chữ nhật](#rectangle)
3. [Vẽ hình tròn](#circle)
4. [Vẽ hình đa giác](#polylines)
5. [Vẽ văn bản](#text)

## Vẽ đường thẳng<a name="line"></a>

Để vẽ một đường thẳng, bạn cần xác định 2 điểm (điểm bắt đầu và điểm kết thúc).

```python
import cv2
import numpy as np

img = cv2.imread('1.png')

# Vẽ một đường thẳng màu trắng từ điểm (100, 100) đến (400, 400)

# img (ảnh, frame cần vẽ)
# (100,100) => tọa đồ bắt đầu
# (400,400) => tọa độ kết thúc
# (255,255,255) => Hệ màu BGR
# 2 => độ dày của đường thẳng (2px)
cv2.line(img, (100, 100), (400, 400), (255, 255, 255), 2)

# Hiển thị hình ảnh
cv2.imshow("Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Vẽ hình chữ nhật<a name="rectangle"></a>

Để vẽ hình chữ nhật, bạn cần xác định tọa độ của góc trên bên trái và góc dưới bên phải của hình chữ nhật.

```python

...

# Vẽ hình chữ nhật với đường viền có 2px
cv2.rectangle(img, (100,100), (300,300), (255,255,255), 2)

# Vẽ hình chữ nhật fulfilled
# Điền thông số độ dày là -1 => fulfilled
cv2.rectangle(img, (100,100), (300,300), (255,255,255), -1)

```

## Vẽ hình tròn<a name="circle"></a>

Để vẽ hình tròn, bạn cần xác định tâm và bán kính của hình tròn.

```python

# Tâm của đường tròn ở (250,250)
# Bán kính => 100px
# Đường viền 2 (dùng -1 để fulfilled)
cv2.circle(img, (250, 250), 100, (0, 0, 255), 2)

```

Để vẽ hình ellipse, bạn cần xác định tâm và độ dài trục x, trục y.

```python
# (400,400) => tâm
# (100,50) => độ dày x: 100, độ dài trục y: 50
# 0 => Góc quay của ellipse
# 0, 360 => Góc bắt đầu, góc kết thúc
cv2.ellipse(img, (400,400), (100,50), 0, 0, 360, (255,255,0), 2)

```

## Vẽ hình đa giác<a name="polylines"></a>

Vẽ đa giác bằng cách xác định tất cả các điểm đỉnh của nó.

```python
import cv2
import numpy as np

# Cần chuyển đổi array chứ các tọa độ đỉnh sang array numpy (đối tượng array của numpy)

# Lần lượt khai báo các đỉnh vào list
pts_list = [[250, 150], [150, 350], [350, 350]]
pts_list_2 = [[400, 100], [450, 250], [350, 200]]

# Chuyển đổi list thành array (numpy)
# np.int32 => chỉ định kiểu dữ liệu cho array
pts_nparray = np.array(pts_list, np.int32)
pts_nparray_2 = np.array(pts_list_2, np.int32)


img = cv2.imread('1.png')

# img => ảnh, frame
# [pts_nparray, pts_nparray_2] => tạo 1 mảng chứa array đỉnh (có thể chứa nhiều array đỉnh)
# isClosed => Nối điểm đầu và điểm cuối
# thickness: độ dày đường viền
cv2.polylines(img, [pts_nparray, pts_nparray_2], isClosed=True, color=(0, 255, 0), thickness=2)

```

## Vẽ văn bản<a name="text"></a>

```python
font = cv2.FONT_HERSHEY_SIMPLEX
# 100, 500 (xác định tọa độ bắt đầu)
# font => fontFace
# fontScale => kích thước tỉ lệ font chứ
#
cv2.putText(img, "Hello AI", (100,500), font, fontScale:2, (255,255,255),2)

```
