def pn(n):
    divsum=0
    for i in range(1,n):
        if n%i==0:
            divsum=divsum+i
    if divsum==n:
        print("Perfect number")
    else:
        print("Not perfect number")
pn(44)