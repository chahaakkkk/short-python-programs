def twosum(l,t):
    d={}
    #[2,7,11,15] t=9
    for i in range(len(l)):
        com=t-l[i]

        if com in d:
            return [d[com],i]
        
        d[l[i]]=i

print(twosum([2,7,11,15],t=9))