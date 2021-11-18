import cv2

src = cv2.imread('./image.jpg')

height = int((100*src.shape[0])/src.shape[1])
size = (100, height)
dst = cv2.resize(src, size)
cv2.imwrite('small.jpg', dst)