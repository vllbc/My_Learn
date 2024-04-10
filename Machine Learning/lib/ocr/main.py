from asyncore import read
import paddlehub as hub
import easyocr
import cv2
import pathlib
import docx

ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")
# img_path = r"D:\Work_Space\vllbc_project\My_Learn\Machine Learning\model_learn\ocr\image\1.png"
img_path = r"./image/5.png"

img = cv2.imread(img_path)
temp = ocr.recognize_text(images=[img])
print(temp)
# reader = easyocr.Reader(["ch_sim", "en"])
# # img = cv2.imread(img_path)
# print(reader.readtext(img_path))