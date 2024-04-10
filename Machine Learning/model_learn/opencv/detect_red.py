import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

red1=np.array([170,100,100]) 
red2=np.array([179,255,255]) 

def detect_red_img(img):
    cv2.imshow("Image", img)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, red1, red2)
    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("hsv", res)
while True:
    ret, img = cap.read()
    detect_red_img(img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()