def rev(li):
    l=0
    r=len(li)-1
    while l<r:
        li[l],li[r]=li[r],li[l]
        l=l+1
        r=r-1
    return li

print(rev([1,2,3,4]))
