
texts = input().split()
for text in texts[1:]:
    res = []
    start = 0
    for i in range(len(text)):
        if (i - start == 5) or i == len(text) - 1:
            res.append(list(text[start:i+1]))
            start = i + 1
    while len(res[-1]) != 6:
        res[-1].append(chr(0))
    nums = [0] * 6
    for r in res:
        nums[0] += ord(r[0])
        nums[1] += ord(r[1])
        nums[2] += ord(r[2])
        nums[3] += ord(r[3])
        nums[4] += ord(r[4])
        nums[5] += ord(r[5])
    for i in range(6):
        sums = sum(map(int, str(nums[i])))
        while len(str(sums)) > 1:
            sums = sum(map(int, str(sums)))
        nums[i] = sums
    print(''.join(map(str, nums)))
