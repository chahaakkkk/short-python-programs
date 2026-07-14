def pn(n):
    divsum=1
    for i in range(2,n):
        if n%i==0:
            divsum=divsum+i
    if divsum==n:
        print("Perfect number")
    else:
        print("Not perfect number")
pn(44)