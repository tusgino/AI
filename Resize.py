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
