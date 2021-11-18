import cv2

src = cv2.imread('./image.jpg')
img_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()