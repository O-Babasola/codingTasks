#Practical Task 1
count = 0
sum_of_num = 0
total = 0
while True:
    num = int(input("Please enter a number: "))
    if num != -1:
        count += 1
        print(f"The number of times you have inputed is {count}")
        sum_of_num += num
        print(f"The sum of the number(s) entered so far is {sum_of_num}")
        total = sum_of_num / count
        print(f"The average of the numbers you have entered is {total}")
    else:
        if num == -1:
            print("Error! The number you have entered is -1.")
            print(f"The last remaining average of the numbers you have entered is {total}")
            break
