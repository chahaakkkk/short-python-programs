def pellindrom(s):
    # if s==s[::-1]:
    #     print("pelindome")
    # else:
    #     print("not pelindrome")
    # rev=""
    # for i in s:
    #     rev=i+rev
    # print(rev)
    # if rev==s:
    #     print("pellindrom")
    # else:
    #     print("not pellindrome")    

    l=0
    r=len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
            break
        l=l+1
        r=r-1
    return True

print(pellindrom("abc"))