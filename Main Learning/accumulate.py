import itertools

test_list = [i for i in range(1, 11)]
                                                             
for i in itertools.accumulate(test_list):                    
    print(i, end=",")                                        
print()                                                      
for i in itertools.accumulate(test_list, lambda x, y: x * y):
    print(i, end=',')
