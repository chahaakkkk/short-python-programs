def minele(l):
    min=l[0]
    for i in l:
        if i<min:
            min=i
    return min

print(minele([5, 3, 8, 1, 9, 4,0]))