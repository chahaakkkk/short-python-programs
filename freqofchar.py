def feq(s):
    f={}
    for i in s:
        if i in f:
            f[i]=f[i]+1
        else:
            f[i]=1
    return f

print(feq("hellooo"))