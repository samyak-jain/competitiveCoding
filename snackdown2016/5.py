def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far,max_ending_here

print max_subarray([1,-2,3,-2,5])
    """if not all(i<0 for i in l):
        l.append(0)
        lst = []
        for x in range(n):
          d = l[:]
          del d[x]
          ls = d[mssl(d)[0]:mssl(d)[1]]
          lst.append(sum(ls))
        lstt.append(max(lst))
    else:
        lstt.append(max(l))"""
                """ls1 = l[mssl(l)[0]:mssl(l)[1]]
        if not all(i>0 for i in ls1):
            ls1.remove(min(ls1))
        l.remove(min(l))
        ls = l[mssl(l)[0]:mssl(l)[1]]
        lstt.append(max(sum(ls),sum(ls1)))"""
        """elif a==k:
                lis.append(wtup[-1][1])
                break
            elif b==k:
                lis.append(wtup[0][1])
                break"""