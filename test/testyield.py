from typing import Iterable


def test_format(datas: Iterable[str], max_len: int):
    for data in datas:
        if len(data) > max_len:
            yield data[:max_len] + '...'
        else:
            yield data


print(list(test_format(['vllbc', 'test_for_this_function', 'good'],5)))
