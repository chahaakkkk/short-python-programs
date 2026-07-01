def add(num):
    a=0
    while num>0:
        dig=num%10
        a=a+dig
        num=num//10

    return a

print(add(123))