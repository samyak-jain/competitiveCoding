T = input()
ls = []
while T:
    n = input()
    a = (raw_input()).split()
    if n%2: ls.append("Derek")
    else: ls.append("Henry")
    T-=1

for i in ls:
  print i