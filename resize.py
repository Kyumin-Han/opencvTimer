import cv2

src = cv2.imread('./image4.jpg')
print(src.shape)

height = int((100*src.shape[0])/src.shape[1])
size = (100, height)

dst = cv2.resize(src, size)
cv2.imshow('image', src)
cv2.imshow('scaling', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()