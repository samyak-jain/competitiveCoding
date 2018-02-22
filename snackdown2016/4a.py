t=0
flag=0
a,b,c,d = [float(i) for i in raw_input().split()]
while flag!=1:
    for i in range(1000):
        y = abs((a-b+(c*i)-t)/d)
        if isinstance(y,int) and y>0:
            flag=1
            break
    if flag==0:
        t+=1
    
print t,y,i