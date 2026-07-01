# def righttri(n):
#     for i in range(n):
#         for j in range(n):
#             if i+j>=n-1:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         print()
# righttri(5)

# def righttri(n):
#     for i in range(n):
#         print("  "*(n-i-1),end="")
#         print("* "*(i+1))
# righttri(5)

def righttri(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            print(chr(65+i),end=" ")
        print()
            
righttri(5)



