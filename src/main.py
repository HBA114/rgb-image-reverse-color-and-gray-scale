import cv2 as cv
from image_operations import convert_to_gray_scale, convert_to_reverse

file_path = "images/profile.jpg"

image = cv.imread(file_path, 1)
reversed_RGB = convert_to_reverse(image)
gray_scale_image = convert_to_gray_scale(image)
reverse_image = convert_to_reverse(gray_scale_image)

cv.imshow("Original", image)
cv.imshow("Reversed RGB", reversed_RGB)
cv.imshow("Gray Scale", gray_scale_image)
cv.imshow("Reversed", reverse_image)

cv.waitKey(0)
cv.destroyAllWindows()