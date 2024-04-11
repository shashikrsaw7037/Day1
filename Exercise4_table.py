# Exercise 4: Write a program to print multiplication table of a given number
print("Using forloop") 
x=int(input("Enter a number"))
n =11
for i in range(n):
    if i==0:
        continue
    print(i*x) 
    

print("Using whileloop") 
x=int(input("Enter a number \n"))
print("*"*20)
n =10
i=1
while i<=n:
    print(i*x)
    i+=1
