def digtoword(n):
    word=""
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    while n>0:
        dig=n%10
        word=d[dig]+" "+word
        n=n//10

    print(word)

digtoword(123)

