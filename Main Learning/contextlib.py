from contextlib import contextmanager,ContextDecorator


@contextmanager
def open_file(filename, methods="r"):
    print(f"打开了文件{filename}")
    res_file = open(filename, mode=methods)  # __enter__方法 这里也可以是自己定义的类

    try:
        yield res_file    # 相当于在__enter__方法里面返回self  yield后面为空的话就不用as了
    except Exception as e:
        print("有错误发生", e)  # __exit__方法里的错误处理
    finally:
        res_file.close()  # __exit__


with open_file("testvim.txt") as fp:
    print(fp)

# name = "水浒传"
# @contextmanager
# def add_book():
#     print("《", end="")
#     yield
#     print("》")


# with add_book():
#     print(name, end="")
