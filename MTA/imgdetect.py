import cv2
img = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('a2',img)
cv2.waitKey(0)
cv2.destroyAllWindows()