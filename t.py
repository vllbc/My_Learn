T = int(input())
for i in range(T):
  n = int(input())
  arr = input().split()
  arr = list(map(int, arr))
  if len(arr) <= 2:
      print("No")
  max_a = max(arr)
  max_idx = arr.index(max_a) 
  is_yx = lambda nums: sorted(nums) == nums and len(set(nums)) == len(nums) and len(nums) > 1
  is_yx_right = lambda nums: sorted(nums, reverse=True) == nums and len(set(nums)) == len(nums) and len(nums) > 1
  res = "Yes" if is_yx(arr[:max_idx+1]) and is_yx_right(arr[max_idx:]) else "No"
  print(res)
  
            