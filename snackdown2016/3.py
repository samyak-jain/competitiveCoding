from copy import deepcopy
T = input()
ls = []
def dupli(the_list,np):
    counts = [0] * np
    for n in the_list:
        counts[n] += 1
    return [[i, counts[i]] for i in range(np) if counts[i]]
while T:
    s = (raw_input()).split()
    w = dict((c, s[0].count(c)) for c in set(s[0]))
    k = int(s[1])
    flag1 = 0
    flag2 = 0
    wval = w.values()
    wtup = dupli(wval,max(wval)+1)
    wtup = sorted(wtup,key= lambda x:x[0], reverse=True)
    if k<(max(wval)-min(wval)):
        lis = []
        lss = []
        for i in range(k,-1,-1):
            lis = []
            dwtup = deepcopy(wtup)
            while 1:
                if len(dwtup)==1:
                    break
                elif len(dwtup)==2:
                    a = dwtup[0][0] - dwtup[1][0]
                    b = dwtup[0][0] - dwtup[1][0]
                else:
                    a = dwtup[0][0] - dwtup[-2][0]
                    b = dwtup[1][0] - dwtup[-1][0]
                if a==i or b==i:
                    if (dwtup[-2][1]+dwtup[-1][1])<(dwtup[1][1]+dwtup[0][1]): 
                        lis.append(dwtup[-1][1])
                        break
                    else: 
                        lis.append(dwtup[0][1])
                        break
                else:
                    if len(dwtup)==2:
                        if i!=0 or (dwtup[0][0]*dwtup[0][1])<=(dwtup[1][0]*dwtup[1][1]):
                            lis.append(dwtup[0][1])
                            dwtup[0][0]-=1
                            if dwtup[0][0]==0: del dwtup[0]
                        else:
                            lis.append(dwtup[1][1])
                            dwtup[1][0]-=1
                            if dwtup[1][0]==0: del dwtup[1]
                    else:
                        if (dwtup[-2][1]+dwtup[-1][1])<(dwtup[1][1]+dwtup[0][1]): 
                            lis.append(dwtup[-1][1])
                            dwtup[-1][0]-=1
                            if dwtup[-1][0]==0: del dwtup[-1]
                        else:
                            lis.append(dwtup[0][1])
                            dwtup[0][0]-=1
                            if dwtup[0][0]==0: del dwtup[0]
            lss.append(sum(lis))
        ls.append(min(lss))
    elif len(wval) == 1:
        ls.append(0)
    else:
        ls.append(0)
    T-=1

for i in ls:
  print i