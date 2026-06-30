# def anagram(s1,s2):
#     if len(s1)!=len(s2):
#         print("Not anagram")
#     else:
#         if sorted(s1)==sorted(s2):
#             print("anagram")
#         else:
#             print("not anagram")

# anagram("chahak","chahah")


def anagram(s1,s2):
    if len(s1)!=len(s2):
        print("not anagram")
    fq={}
    for i in s1:
        if i in fq:
            fq[i]=fq[i]+1
        else:
            fq[i]=1
    for i in s2:
        if i not in fq:
            print("not anagram")
            break
        fq[i]=fq[i]-1

        if fq[i]<0:
            print("not anagram")
            break
    print("anagram")
anagram("silent","listen")
