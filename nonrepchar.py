def non_rep(s):
    f={}
    for i in s:
        if i in f:
            f[i]=f[i]+1
        else:
            f[i]=1
    for i in f.keys():
        if f[i]==1:
            print(i,end=" ")

non_rep("hello")