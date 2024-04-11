# /Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.

# number  = 123
# count = 0
# while number > 0:
#     number = number / 10
#     count +=1
#     print(count)
    
# num = 75869
# count = 0
# while num > 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10

#     # increment counter by 1
#     count +=1
# print("Total digits are:", count)



number  = 123
while number>0:
    r = number % 10
    print(r ,end="")
    number = number // 10
print(r)     
































# num = 75869
# count = 0
# i =0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     nu = num % 10
#     i+=1
#     print("Total digits are:",i, nu)
#     # increment counter by 1
#     count = count + 1
# # print("Total digits are:", num)



# num = 76542
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)

# print(~101)
# Initially , I convert into decimal to binary .It is 1100101
# Then I used complement 0011010