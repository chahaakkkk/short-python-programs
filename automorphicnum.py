def auto(n):
    sqr=str(n*n)
    n=str(n)
    if n[-1]==sqr[-1]:
        return True
    else:
        return False
    
print(auto(5))