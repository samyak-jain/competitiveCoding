ls=[]
for car in range(input()):
    flag=0
    nextpos = 0
    d1=0
    d2=0
    n,k = [int(i) for i in raw_input().split()]
    a = [int(i) for i in raw_input().split()]
    aso = sorted(a,key=abs,reverse=True)
    p = reduce(lambda x,y:x*y,aso[:k])
    if len(aso)==2:
        if k==1: ls.append(max(aso))
        else: ls.append(p)
    elif p<0:
        ar1n = [i for i in aso[:k] if i<0]
        ar1p = [i for i in aso[:k] if i>0]
        ar2n = [i for i in aso[k:] if i<=0]
        ar2p = [i for i in aso[k:] if i>=0]
        try:
            lastneg = max(ar1n)
        except ValueError:
            lastneg = 1
        try:
            nextpos = max(ar2p)
        except ValueError:
            nextpos = 1
            flag=1
        try:
            lastpos = min(ar1p)
        except ValueError:
            lastpos = 1
            flag=1
        try:
            nextneg = min(ar2n)
        except ValueError:
            nextneg = 1
        if nextpos==0 and not aso.count(0)>=1:
            nextpos = lastpos
        if nextneg==0 and not aso.count(0)>=1:
            nextneg = min(aso[k:])
        if flag:
            lastneg = min(ar1n)
        d1 = p
        d2 = p
        if all(i<0 for i in a):
            d2/=lastneg
            d2*=nextneg
            d1=d2
        else:
            d1/=lastneg
            d1*=nextpos
            d2/=lastpos
            d2*=nextneg
        ls.append(max(d1,d2))
    else:
        ls.append(p)
    
for i in ls:
    print (i%(7 + (10**9)))