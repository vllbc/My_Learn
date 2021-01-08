def merge(intervals):
        res = intervals[:]
        if not res:
            return []
        res.sort(key=lambda i:i[0])
        n = len(res) - 1
        for i in range(0,n):
            if res[i][1] < res[i+1][0]:
                continue
            else:
                res[i+1] = [res[i][0],max(res[i][1],res[i+1][1])]
                res[i] = res[i-1]
        ress = []
        for i in res:
            if i not in ress:
                ress.append(i)
        print(ress)
merge(
[[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]])