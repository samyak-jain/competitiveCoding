t = input()
ls = []
def check(a):
    for i in range(n-2):
        if a[i]==a[i+1]==a[i+2]:
            return 1
    return 0

while t:
    n = input()
    c = [int(i) for i in raw_input().split()]
    if check(c):
        ls.append("Yes")
    else:
        ls.append("No")
    t-=1

for i in ls:
    print i