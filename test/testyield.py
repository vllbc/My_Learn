'''
Author: your name
Date: 2021-02-06 23:26:14
LastEditTime: 2021-03-07 19:13:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \My_Learn\test\testyield.py
'''
from typing import Iterable


def test_format(datas: Iterable[str], max_len: int):
    '''
    description: 
    param {}
    return {*}
    '''
    for data in datas:
        if len(data) > max_len:
            yield data[:max_len] + '...'
        else:
            yield data


print(list(test_format(['vllbc', 'test_for_this_function', 'good'],5)))
