# import jieba
# pu = """
# 我住长江头，君住长江尾。日日思君不见君，共饮长江水。
# 此水几时休，此恨何时已。只愿君心似我心，定不负相思意。
# """
# l = jieba.lcut(pu)

# from collections import Counter
# counts = Counter(l)
# print(dict(sorted(zip(counts.keys(),counts.values()),key=lambda x:-x[1])))
# l = [1,3,5,8,10]
# print(next(i for i in l if i%2==0))
biaodashi = input()
while True:
    a,b = map(int,input().split())
    print(eval(biaodashi))
