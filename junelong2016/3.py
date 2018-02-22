def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def dupli(the_list,np):
    counts = [0] * np
    for n in the_list:
        counts[n] += 1
    return [[i, counts[i]] for i in range(np) if counts[i]]
def x():   
    n = input()
    while 1:
        a = primes(n)
        w = dupli(a,len(a)+1)
        if n==1:
            return "Chef"
        elif len(w)==1:
            return "Chef"
        else:
            n -= w[0][0]**w[0][1]
        if n<0:
            return "Misha"
        else:
            return -1

t = input()
while t:
    print x()
    t-=1