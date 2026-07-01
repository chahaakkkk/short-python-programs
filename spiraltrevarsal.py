def rt(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[i][j],end=" ")



l=[[1,2,3],
   [4,5,6],
   [7,8,9]]
rt(l)
print()

def ct(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            print(l[j][i],end=" ")
ct(l)
print()

def st(l):
    top=0
    buttom=len(l)-1
    left=0
    right=len(l[0])-1

    while top<=buttom and left<=right:
        
        for i in range(left,right+1):
            print(l[top][i])
        top=top+1

        for i in range(top,buttom+1):
            print(l[i][right])
        right=right-1

        if top<=buttom:
            for i in range(right,left-1,-1):
                print(l[buttom][i])
            buttom=buttom-1

        if left<=right:
            for i in range(buttom,top-1,-1):
                print(l[i][left])
            left=left+1

st(l)


