
# manipulation.py is practical task 1
str_manip= input("Enter a sentence: ")
length_manip = len(str_manip)
print(length_manip)
last_char = str_manip[-1]
print(last_char)

last_3_char= str_manip[-3:]
print(last_3_char)
reverse_last_3 = last_3_char[::-1]
print(reverse_last_3)

first_3_char = str_manip[0:3]
print(first_3_char)
last_2_char = str_manip[-2:]
print(last_2_char)

five_letter= first_3_char + last_2_char
print(five_letter)


for x in str_manip:
    new_manip= str_manip.replace(last_char, "@")
    print(new_manip)
    break
