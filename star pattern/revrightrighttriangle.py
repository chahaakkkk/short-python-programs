def triangle(n):
    for i in range(n):
        for j in range(i):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")
        print()

triangle(5)