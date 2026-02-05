def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
def gcd_list(arr):
    g=arr[0]
    if len(arr)==1:
        return g
    else:
        for i in range(1,len(arr)):
            g=gcd(g,arr[i])
        return g
print(gcd_list([36]))        