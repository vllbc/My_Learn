def honer(n,A,B,C):
    if n == 1:
        print(f"move:{A}---->{C}")
    else:
        honer(n-1,A,C,B)
        print(f"move:{A}---->{C}")
        honer(n-1,B,A,C)
honer(3,'A','B','C')