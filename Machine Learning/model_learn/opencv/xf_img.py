import cv2
import numpy as np

img_path = "./shuiyin.jpg"

img = cv2.imread(img_path)
h, w, d = img.shape[0:3]

thresh = cv2.inRange(img, np.array([240, 240, 240]), np.array([255, 255, 255]))

kernel = np.ones((3, 3), np.uint8)


hi_mask = cv2.dilate(thresh, kernel, iterations=1)
specular = cv2.inpaint(img, hi_mask, 5, flags=cv2.INPAINT_TELEA)

cv2.namedWindow("Image", 0)
cv2.resizeWindow("Image", int(w / 2), int(h / 2))
cv2.imshow("Image", img)

cv2.namedWindow("newImage", 0)
cv2.resizeWindow("newImage", int(w / 2), int(h / 2))
cv2.imshow("newImage", specular)
cv2.waitKey(0)
cv2.destroyAllWindows()