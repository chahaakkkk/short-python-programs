def fib(n):
#     if n<=1:
#         return n
#     else:
#         return(fib(n-1)+fib(n-2))

# for i in range(7):
#     print(fib(i),end=" ")
    
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
fib(7)
