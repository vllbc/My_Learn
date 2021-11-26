from pathlib import Path


# 把txt文件重命名为csv文件
def unify_ext_with_pathlib(path):
    for fpath in Path(path).glob("*.txt"):
        fpath.rename(fpath.with_suffix(".csv"))

print(Path(".") / "test_pathlib.py")  # Path类型可以使用/运算符
print(Path("testvim.txt").read_text()) # 直接读取文件内容

# .resolve() 取绝对路径
# with_name() 修改文件名 with_suffix()修改后缀名
# 把当前目录下的文件批量重命名
# import os
# from pathlib import Path

# p = Path(".")

# for filepath in p.glob("test_*.py"):
#     name = filepath.with_name(str(filepath).replace("test_",""))
#     filepath.rename(name)
