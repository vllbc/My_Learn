import numpy
from PIL import Image, ImageDraw, ImageFont
import cv2


def cv2ImgAddText(img, text, left, top, textColor=(0,0,0), textSize=100):
    if (isinstance(img, numpy.ndarray)):  #判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    fontText = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    draw = ImageDraw.Draw(img)
    draw.text((left, top), text, textColor,font=fontText)
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

img = cv2.imread("test2.jpg")
img = cv2ImgAddText(img,"田奔",140,100)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
