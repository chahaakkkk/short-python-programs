def frq_arr(s):
    fq=[0]*26
    for i in s:
        fq[ord(i)-97]=fq[ord(i)-97]+1
    return fq


def unq_str(s):
    l=frq_arr(s)
    flag=True
    for i in l:
        if i>1:
            flag=False
            break
    return flag
print(unq_str("pqrdt"))