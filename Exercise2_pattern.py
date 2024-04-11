# i is using for row
# j is row for column

# n = int(input())
# for i in range(n):# row
#     for j in range(n):
#         print(n,end=" ") 
#     print()    
    
n = int(input("Enter a number" ))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1    
    
# O/P is
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5    