#T08 Task 2
#try block allows you to test a block of code for errors
#except block allows you to handle the error
#else block allows you execute the code when there is no error


while True:
    try:
        students = int(input("Please enter the number of students that are registering: ")) #asks for user input and stores value as students
    except ValueError:
        print("Error. Please try again!")
        continue #continues back to start of code if incorrect value is entered
    else:
        break


for x in range(1,students + 1):
    with open("reg_form.txt", "a") as file: #opens reg_form text file and writes and adds data to it.
        while True:
            try:
                student_ID = int(input("Please enter your student ID: ")) #asks for user input and stores value as student_ID.   
                if len(str(student_ID)) != 7: # checks that length is not equal to 7. If it is not equal to 7 then ask user for an input of student ID again
                    print("Student ID should be 7 in length. Please try again.")
                    continue
                else:
                    break

            except ValueError:
                print("Incorrect Entry!. Please try again.")
                continue #continues back to start of code if incorrect value is entered
            else:
                break
        file.write(f"Student ID is: {student_ID}" + "\n \n------------------\n \n") #finally adds student ID to file stored as reg_form
        
    
    