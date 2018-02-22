for abc in range(input()):
    lstt=[]
    n,k,e,m = [int(i) for i in raw_input().split()]
    for i in range(n-1):
        lstt.append([int(i) for i in raw_input().split()])
    sums = map(sum,lstt)
    sosum = sorted(sums,reverse=True)
    
    