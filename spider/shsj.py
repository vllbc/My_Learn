def test(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    print(list(zip(*args)))


test([1, 2], [2, 3], [3, 4], [4, 5], [5, 6], a="1", b="2")
