import cv2
import imutils

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

# Xoay ảnh với thư viện imutils
rotated_image_2 = imutils.rotate(image, angle["90"])

cv2.imshow("Image", image)
cv2.imshow("Rotated Image", rotated_image)
cv2.imshow("Rotated Image 2", rotated_image_2)

cv2.waitKey(0)
cv2.destroyAllWindows()



