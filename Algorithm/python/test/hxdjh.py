text = input()
import re

try:
    text = re.sub(r"[^\-\da-fA-F]","",text)
    if text[0] == '-':
        text = text.replace("-",'')
        print(-int(text,16))
    else:
        text = text.replace("-",'')
        print(int(text,16))
except:
    print("0")
