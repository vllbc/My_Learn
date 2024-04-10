from asyncore import read
import paddlehub as hub
import easyocr
import cv2
import pathlib
import docx

# img_path = r"D:\Work_Space\vllbc_project\My_Learn\Machine Learning\model_learn\ocr\image\1.png"
img_path = r"D:\Work_Space\vllbc_project\小红书图片\highlightclean\219.jpg"

# doc_path = "./doc" # 文档路径(文件夹)
# for path in pathlib.Path(img_path).iterdir():
#     doc = docx.Document()
#     name = path.name.split('.')[0]
#     image = cv2.imread(str(path))
#     temp = ocr.recognize_text(images=[image])
#     for t in map(lambda x:x["text"], temp[0]["data"]):
#         doc.add_paragraph(t)
#     doc.save(f"{doc_path}/{name}.docx")


reader = easyocr.Reader(["ch_sim", "en"])
# img = cv2.imread(img_path)
print(reader.readtext(img_path))