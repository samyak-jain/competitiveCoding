from datetime import datetime
def lcs(S):
    S += S
    f = [-1] * len(S)
    k = 0
    for j in xrange(1,len(S)):
        sj = S[j]
        i = f[j-k-1]
        while i != -1 and sj != S[k+i+1]:
            if sj < S[k+i+1]:
                k = j-i-1
            i = f[i]
        if sj != S[k+i+1]:
            if sj < S[k]:
                k = j
            f[j-k] = -1
        else:
            f[j-k] = i+1
    return k

s = raw_input()
ls = []
for ab in range(input()):
    n = [int(i) if i.isalpha() else i for i in raw_input().split()]
    st = datetime.now()
    if n[0]:
        subs = s[n[1]-1:n[2]]
        p = lcs(subs)
        ls.append((subs[p:] + subs[:p])[n[3]-1])
    else:
        s = s[:n[1]-1] + n[2] + s[n[1]:]
    print (datetime.now()-st).total_seconds()

for i in ls:
    print i