def ap(arr):
    if len(arr)<2:
        return False
    d=arr[1]-arr[0]
    for i in range(2,len(arr)):
        if arr[i]-arr[i-1]!=d:
            return False
    return True

print(ap([1,2,3,4,5]))
