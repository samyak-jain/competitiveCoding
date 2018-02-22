from datetime import datetime
t = input()
ls = []
def magic(n):
    for i in str(n):
        if int(i)%2: return 0
    return 1
    
while t:
    k = input()
    start = datetime.now()
    j=0
    c=0
    while 1: 
        if magic(j): c+=1
        if c==k: break
        j+=1
    ls.append(j)
    t-=1
    print (datetime.now()-start).total_seconds()

for i in ls:
    print i