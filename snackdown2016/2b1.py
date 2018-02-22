n,k = [int(i) for i in raw_input().split()]
a = [int(i) for i in raw_input().split()]
b = a
while not k%2:
    a=b
    b=[]
    a = sorted(a,reverse=True)
    for i in a:
        if i<0: break
    a = a[:i] + sorted(a[i:])
    for i in range(0,len(a)-1,2):
        if a[i]*a[i+1]>0:
            b.append(a[i]*a[i+1])
        else:
            b.append(a[i])
            b.append(a[i+1])
    k/=2

ap = [i for i in a if i>0]
an = [i for i in a if i<0]