def replace(s,sub,newsub):
    # print(s.replace(sub,newsub))
    n=""
    l=len(sub)
    for i in range(len(s)):
        if s[i:i+l]==sub:
            n=s[:i]+newsub+s[i+l:]
    print(n)




replace("hello world everyone","world","python")