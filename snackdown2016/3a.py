from fractions import gcd
ls = []
for dfj in range(input()):
    a,b,c,d = [int(i) for i in raw_input().split()]
    g = gcd(c,d)
    ls.append(min((a-b)%g,(b-a)%g))

for i in ls:
    print i