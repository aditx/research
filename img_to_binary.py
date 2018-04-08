import cv2

img = cv2.imread('resources/img01.jpg', 0)
ret, thresh = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

cv2.imwrite('resources/threshold_image.jpg', thresh)
cv2.imshow('Threshold', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()