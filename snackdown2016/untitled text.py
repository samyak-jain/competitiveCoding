    """a = input()
    start = datetime.now()
    #a = [int(i) for i in a]
    flag = 0
    while max(a)!=1:
        a.sort(reverse=True)
        if 1<a[0]<6:
          a[0] = 1
        else:
          a[0]/=6
        flag+=1

    if not flag%2: ls.append("Henry")
    else: ls.append("Derek")
    T-=1
    print (datetime.now() - start).total_seconds()"""