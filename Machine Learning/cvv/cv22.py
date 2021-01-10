import cv2

filepath = 'test.jpg'
img = cv2.imread(filepath)
cv2.namedWindow('Image')
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destoryAllWindows()