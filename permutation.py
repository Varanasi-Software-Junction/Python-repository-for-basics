def permute(l,i,n):
    if i>n-1:
        print(l)
        return

    for r in range(n):
        slice=l[:i]
        if r in slice:
            continue
        l[i]=r
        permute(l,i+1,n)
l=[1,2,3]
n=len(l)
permute(l,0,n)








