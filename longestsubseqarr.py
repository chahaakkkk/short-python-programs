def longest(l):
    count=0
    start=None
    l=set(l)
    for i in l:
        if i-1 not in l:
            curr=i
            length = 1

            while curr+1 in l:
                curr=curr+1
                length=length+1

        if length>count:
            count=length
            start=i
    print("longest seq")
    for i in range(start,count+1):
        print(i,end=" ")
    print("max lenght: ", count)

longest([100, 4, 200, 1, 3, 2])