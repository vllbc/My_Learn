# letters = 'abcdefghijklmnopqrstuvwxyz'

# def re_e(c):
#     if c.isalpha():
#         ind = letters.index(c)
#         ind = (ind+2)%26#大于26就回去
#         return letters[ind]
#     else:
#         return c
# text  = "map"
# last =""
# for i in text:
#     last+=re_e(i)
# print(last)
def two(list,guess):
    list.sort()
    min = 0
    max=len(list)-1
    
    while min<max:
        mid = (min+max)//2
        if(list[mid]<guess):
            min = mid+1
        if(list[mid]>guess):
            max = mid-1
        if(list[mid] == guess):
            return mid
    
print(two([3,2,1,5,6],5))