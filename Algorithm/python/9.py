#翻转图像

class Solution:
    def rotate(matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in list(map(list,map(reversed,zip(*matrix)))):
            matrix.append(i)
        del matrix[:n]