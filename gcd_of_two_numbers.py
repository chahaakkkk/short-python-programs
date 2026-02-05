def gcd(a,b):
    # if a>b:
    #     bigger=a
    #     smaller=b
    # else:
    #     bigger=b
    #     smaller=a
    # while smaller!=0:
    #     temp=smaller
    #     smaller=bigger%smaller
    #     bigger=temp
    # return bigger
    while a!=0:
        temp=a
        a=b%a
        b=temp
    return b
print(gcd(84,56))