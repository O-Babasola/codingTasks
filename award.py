
#award.py is the practical task 3
swimming = int(input("Enter time take for completing swimming: "))
cycling = int(input("Enter time take for completing cycling: "))
running = int(input("Enter time take for completing running: "))
total_minutes = swimming + cycling + running

print(f"The total minutes you took for the triathlon is {total_minutes}")



if total_minutes <= 100:
    print("You have won the Provinical Colours award")
elif total_minutes >=101 and total_minutes <=105:
    print("You have won the Provinical Half Colurs award")
elif total_minutes >= 106 and total_minutes <=110:
    print("You have won the Provinical Scroll award")
elif total_minutes >= 111:
    print("You have will not receive an award")
else:
    print("Invalid input")

#Or can have the if elif-else statement as just :

"""
if total_minutes <= 100:
    print("You have won the Provinical Colours award")
elif total_minutes >=101 and total_minutes <=105:
    print("You have won the Provinical Half Colurs award")
elif total_minutes >= 106 and total_minutes <=110:
    print("You have won the Provinical Scroll award")
else:
    print("You have will not receive an award")
"""