import cv2

image = cv2.imread("01.png")


blurred_image = cv2.blur(image, (9, 9))
gaussian_blurred_image = cv2.GaussianBlur(image, (9, 9), 0)
median_blurred_image = cv2.medianBlur(image, 7)
bilateral_blurred_image = cv2.bilateralFilter(image, 9, 75, 75)


cv2.imshow("Image", image)

cv2.imshow("Blur Image", blurred_image)
cv2.imshow("Gaussian Blur Image", gaussian_blurred_image)
cv2.imshow("Median Blur Image", median_blurred_image)
cv2.imshow("Bilateral Blur Image", bilateral_blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()