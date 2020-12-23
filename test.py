lists = ["flower","flow","flight"]
li = list(map(set,zip(*lists)))
print(li)
