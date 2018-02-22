n,q = map(int,raw_input().split())
a = map(int,raw_input().split())
ls = []
t1 = max(a)
t2 = min(a)
while q:
    t = input()
    if t1>=t>=t2: ls.append("Yes")
    else: ls.append("No") 
    q-=1

for i in ls:
    print i