def power(base,p):
    # print(base**p)
    result =1
    for i in range(p):
        result=result*base

    print(result)


power(2,5)