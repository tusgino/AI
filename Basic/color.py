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