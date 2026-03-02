def con(l):
    flag=True
    for i in range(len(l)-1):
        if l[i]!=l[i+1]-1:
            flag=False
            break

    if flag==True:
        return l
    else:
        return -1
    
l=[1,2,3,4,6]
print(con(l))


def conwindow(l,k):
    nl=[]
    for i in range(len(l)-k+1):
        flag=True
        for j in range(k):
            if l[j]!=l[j+1]-1:
                flag=False
                break
        if flag==True:
            nl.append(i+k-1)
        else:
            nl.append(-1)
    return nl

print(conwindow([1,2,3,4,3,2,5],3))





        
