ti = input()
ls = []
while ti:
    n = input()
    m=""
    if (n%3)==0:
        s = "abcdefghijklmnopqrstuvwxyz"
        t = s[::-1]
        n = n/3
        d = n
        while n>0:
            if n>26:
                d=26
            m += s[:d]
            n-=26
            d=n
        ls.append(m[::-1] + m)
    elif (n%3)==1:
        s = "abcdefghijklmnopqrstuvwxy"
        t = s[::-1]
        n = n/3
        d = n
        while n>0:
            if n>25:
                d=25
            m += s[:d]
            n-=25
            d=n
        ls.append(m[::-1] + 'z' + m)
    else:
        s = "abcdefghijklmnopqrstuvwx"
        t = s[::-1]
        n = n/3
        d = n
        while n>0:
            if n>24:
                d=24
            m += s[:d]
            n-=24
            d=n  
        ls.append('y' + m[::-1] + m + 'z')
    ti-=1
    
for i in ls:
    print i