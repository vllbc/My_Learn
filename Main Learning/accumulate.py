import itertools

test_list = [i for i in range(1, 11)]
<<<<<<< HEAD
                                                             
for i in itertools.accumulate(test_list):                    
    print(i, end=",")                                        
print()                                                      
=======

for i in itertools.accumulate(test_list):
    print(i, end=",")
print()
>>>>>>> a8b720e32694def715bebe2f83bf0621a06052cf
for i in itertools.accumulate(test_list, lambda x, y: x * y):
    print(i, end=',')
