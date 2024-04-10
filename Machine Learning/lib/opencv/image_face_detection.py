<<<<<<<< HEAD:Machine Learning/lib/opencv/image_face_detection.py
import cv2


img = cv2.imread(r"D:\1683070754\FileRecv\highlightclean\highlightclean\194.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

color = (0,255,0)
faceRects = classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # 左眼
        cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)

cv2.imshow("image", img)  # 显示图像
c = cv2.waitKey(10)


cv2.waitKey(0)
========
import cv2


img = cv2.imread(r"D:\1683070754\FileRecv\highlightclean\highlightclean\194.jpg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
classifier = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

color = (0,255,0)
faceRects = classifier.detectMultiScale(
    gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
if len(faceRects):  # 大于0则检测到人脸
    for faceRect in faceRects:  # 单独框出每一张人脸
        x, y, w, h = faceRect
        # 框出人脸
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
        # 左眼
        cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                   color)
        #嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                      (x + 5 * w // 8, y + 7 * h // 8), color)

cv2.imshow("image", img)  # 显示图像
c = cv2.waitKey(10)


cv2.waitKey(0)
>>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf:Machine Learning/model_learn/opencv/image_face_detection.py
cv2.destroyAllWindows()