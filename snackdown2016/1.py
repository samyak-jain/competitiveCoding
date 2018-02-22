T = input()
lst = []
while T:
    n = input()
    a = (raw_input()).split()
    b = (raw_input()).split()
    a = [int(i) for i in a]
    b = [int(i) for i in b]
    c=0
    if b[0]<=a[0]: c+=1
    for i in range(1,n):
      a[i] -= a[i-1]
      if b[i]<=a[i]:
        c+=1
      a[i] += a[i-1]

    lst.append(c)
    T-=1

for i in lst:
  print i
