def bubble(num):
    for i in range(len(num)):
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return(num)

print(bubble([1,5,3,4,0]))