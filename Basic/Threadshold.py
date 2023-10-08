# import cv2
#
# image = cv2.imread("01.png")
#
# # Convert Gray
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# # Threashold
# # THREAD_BINARY: Nếu giá trị pixel > threashold thì pixel đó sẽ được gán giá trị maxval
# # THREAD_BINARY_INV: Nếu giá trị pixel > threashold thì pixel đó sẽ được gán giá trị 0
# ret, threashold_image = cv2.threshold(image_gray, 127,255, cv2.THRESH_BINARY)
#
# if ret:
#     # Nếu convert thành công thì hiển thị ảnh
#     cv2.imshow("Image", image)
#     cv2.imshow("Image Gray", image_gray)
#     cv2.imshow("Threashold Image", threashold_image)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print("Error")

import cv2

image = cv2.imread("01.png")

# Convert to Gray
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Adaptive Threshold

# ADAPTIVE_THRESH_MEAN_C: Giá trị threshold được tính bằng trung bình của các pixel xung quanh
# ADAPTIVE_THRESH_GAUSSIAN_C: Giá trị threshold được tính bằng trung bình có trọng số của các pixel xung quanh
# C: Giá trị thêm vào sau khi tính toán threshold
# blockSize: Kích thước của vùng xung quanh mỗi pixel
# => blockSize càng lớn thì ảnh càng mờ
# Càng nhỏ thì ảnh càng sắc nét
# Càng lớn thì ảnh càng mờ

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
