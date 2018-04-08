import cv2

img = cv2.imread('resources/img03.jpg', 1)
gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite('resources/gray_image03.jpg', gray_image)

cv2.imshow('gray_image03', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()