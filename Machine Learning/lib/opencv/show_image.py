import cv2

filepath = r'./test.jpg'
img = cv2.imread(filepath)
print(img.shape)
# img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.namedWindow('Image')
# cv2.imshow('Image',img)
# cv2.waitKey(0)