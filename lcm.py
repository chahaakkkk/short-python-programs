def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return abs(a*b)//gcd(a,b)

def lcm_list(arr):
    l=arr[0]
    if len(arr)==1:
        return l
    else:
        for i in range(1,len(arr)):
            l=lcm(l,arr[i])
        return l
print(lcm_list([2,1]))