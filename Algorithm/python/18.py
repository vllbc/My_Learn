text = input()
import re
num = re.findall("\d+", text)
print(sum(map(int, num)))