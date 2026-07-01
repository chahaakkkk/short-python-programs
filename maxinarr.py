def maxinarr(l):
    max=l[0]
    for i in range(1,len(l)):
        if l[i]>max:
            max=l[i]

    return max

print(maxinarr([1,5,4,9,2,6]))
    