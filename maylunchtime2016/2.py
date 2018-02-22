T = input()
lst = []
while T:
    s = list(raw_input())
    s = list([i.lower() for i in s])
    k = input()
    if k==len(s):
      lst.append(''.join(s))
    else:
      s.sort()
      lst.append(''.join(s[:k]))
    T-=1

for i in lst:
  print i