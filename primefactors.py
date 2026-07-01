def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

def primef(num):
    for i in range(2,int(num**0.5)+1):
        if prime(i):
            if num%i==0:
                print(i,end=" ")

    if prime(num):
        print(num)
primef(5)


