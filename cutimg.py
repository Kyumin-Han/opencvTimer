import cv2

src = cv2.imread('./image4.jpg')
dst = src[100:200, 100:300]
cv2.imshow('image', src)
cv2.imshow('crop', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()