def absdiff(a, b):
    if (a == b):
        return 0;        
    if (a > b):
        return (a - b);        
    return (b - a);

def min_diff_els(a, b, size):
    i = 0
    j = 0;
    idx1 = 0;
    idx2 = 0;
    mindiff = absdiff(a[0], b[0]);
    
    if (0 == mindiff):
        return 0;
    
    i+=1;
    j+=1;
    while (i < size and j < size):
        cv = absdiff(a[i], b[j]);
        if (cv < mindiff):
            idx1 = i;
            idx2 = j;
            mindiff = cv; 
        
        if (a[i] < b[j]):
            i+=1;
        else:
            j+=1;
    
    return mindiff;
t = eval(input())
ls = []
while t:
    a = [int(i) for i in input().split()]
    x1 = []
    x2 = []
    for i in range(1001):
        x1.append(a[0]+(a[2]*i))
        x2.append(a[1]+(a[3]*i))
        if min_diff_els(x1,x2,len(x1))==0:
            break
    ls.append(min_diff_els(x1,x2,len(x1)))
    t-=1

for i in ls:
    print (i)