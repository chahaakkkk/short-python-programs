def pyramid(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        print("* "*(i+1),end="")
        print()
        
pyramid(5)