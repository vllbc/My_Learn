a = [2,3,41,31,3,2,414,13,13123,221]
def two(lists,target):
    min = 0
    max = len(lists) - 1
    
    while min <= max:
        mid = (max+min)//2
        if target > a[mid]:
            min = mid + 1
        elif target < a[mid]:
            max = mid - 1
        elif target == a[mid]:
            return mid
    return -1
a.sort()
print(a)
print(two(a,1312))
print(two(a,221))