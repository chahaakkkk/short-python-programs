def gcd(n,m):
    if n>=m:
        small=m
    else:
        small=n
    for i in range(small,0,-1):
        if n%i==0 and m%i==0:
            print(i)
            break




gcd(60,36)
    
