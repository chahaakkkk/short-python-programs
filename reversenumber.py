def reverse_num(n):
    #simple code
    # n=int(str(n)[::-1])
    # print(n)

    rev_num=0
    while n>0:
        dig=n%10
        rev_num=rev_num*10+dig
        n=n//10
    print(rev_num)



reverse_num(1230)



