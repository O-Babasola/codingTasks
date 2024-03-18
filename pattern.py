#Practical Task 2

#First set of code tried to create the pattern but used two for loop statements
#But struggled to use an if statement.

for y in range(1, 5, 1):
    print(y * "*")

for x in range(6, 0, -1):
    print(x * "*")

#Second set of code then attempted to use one if statement and one for loop statement


star = "*"
for x in range(1,10):
    if x <= 4:
        print(star) #Prints out each star line until it reaches 4
        star = star + "*"
    else:
        print(star)
        star = star[:-1] # Gets rid of last "*" star from the list of stars




