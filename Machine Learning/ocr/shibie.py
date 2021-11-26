from PIL import Image
import pytesseract
import os

path = os.path.join(os.getcwd(),r"./Machine Learning/shibie/1.png")

text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)
