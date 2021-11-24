from pathlib import Path


# 把txt文件重命名为csv文件
def unify_ext_with_pathlib(path):
    for fpath in Path(path).glob("*.txt"):
        fpath.rename(fpath.with_suffix(".csv"))

print(Path(".") / "test_pathlib.py")  # Path类型可以使用/运算符
print(Path("testvim.txt").read_text()) # 直接读取文件内容
