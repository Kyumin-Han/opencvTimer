import cv2

src = cv2.imread('./image5.jpg')
cv2.imshow('image', src)
cv2.waitKey(0)
cv2.destroyAllWindows()