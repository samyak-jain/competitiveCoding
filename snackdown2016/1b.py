ls = []
for ad in range(input()):
    lst = []
    n,k,e,m = [int(i) for i in raw_input().split()]
    for i in range(n-1):
        lst.append([int(i) for i in raw_input().split()])
    sco = [int(i) for i in raw_input().split()]
    sums = map(sum,lst)
    sosum = sorted(sums,reverse=True)
    if sum(sco)>sosum[0]: ls.append(0)
    else:
        kajshkas = sosum[k-1]+1-sum(sco) 
        if kajshkas<0: ls.append(0)
        elif kajshkas>m:
            ls.append("Impossible")
        else:
            ls.append(kajshkas)

for i in ls:
    print i