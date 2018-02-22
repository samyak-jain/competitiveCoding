def mssl(l):
        best = cur = 0
        curi = starti = besti = 0
        for ind, i in enumerate(l):
            if cur+i > 0:
                cur += i
            else: # reset start position
                cur, curi = 0, ind+1

            if cur > best:
                starti, besti, best = curi, ind+1, cur
        return starti, besti
T = input()
lst = []
lstt = []
while T:
    n = input()
    l = (raw_input()).split()
    l = [int(i) for i in l]
    if all(i>0 for i in l):
        lstt.append(sum(l))
    elif not all(i<0 for i in l):
        lst.append(sum(l))
        for i in range(n):
            if l[i]<0:
                s = l[i]
                del l[i]
                lst.append(sum(l[mssl(l)[0]:mssl(l)[1]]))
                l.insert(i,s)
        lstt.append(max(lst))
    else:
        lstt.append(max(l))
    T-=1

for i in lstt:
  print i