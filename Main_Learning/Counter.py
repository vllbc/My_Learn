from collections import Counter
import random

nums = [random.randrange(1,5) for _ in range(20)]
print(Counter(nums).most_common(3))