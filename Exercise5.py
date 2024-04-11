numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5==0 :
        if i>150:
            continue
        elif i>500 & i<50:
            break
        else:
            print(i)


numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    # check if number is divisible by 5
    elif item % 5 == 0:
        print(item)
