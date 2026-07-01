def add(a,b,c,d):
    print("First Fraction: ",a,"/",b)
    print("Second Fraction: ",c,"/",d)
    if b==d:
        print("Sum: ",a+c,"/",b)
    else:
        print("Sum: ",a*d+b*c,"/",b*d)


add(1,2,1,3)
