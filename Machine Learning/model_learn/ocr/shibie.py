<<<<<<<< HEAD:Machine Learning/lib/ocr/shibie.py
from PIL import Image
import pytesseract
import os

path = os.path.join(os.getcwd(),r"4.jpg")

text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)
========
from PIL import Image
import pytesseract
import os

path = os.path.join(os.getcwd(),r"4.jpg")

text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)
>>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf:Machine Learning/model_learn/ocr/shibie.py
