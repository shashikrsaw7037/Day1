# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Expected output:
# 20 40 60 80 100
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list[1::2])
print("@"*20)
for i in my_list[1::2]:
    print(i)