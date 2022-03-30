from PIL import Image
import pytesseract
import os

path = os.path.join(os.getcwd(),r"4.jpg")

text = pytesseract.image_to_string(Image.open(path), lang='chi_sim')
print(text)
