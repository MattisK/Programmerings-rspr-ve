# Get user input and show it to make sure the user actually has gotten the input
year = float(input("Enter your year: "))
print("Your chosen year is: "+ str(year))

# Function to check wether a certain year is a leap year
def checkLeapYear():

#Define years divided by 100, 400 and 4
    year100 = float(year/100)
    year400 = float(year/400)
    year4 = float(year/4)

    #Checks if a year is divisible by 100, if yes then checks if it is divisible by 400
    if year100/1 - year100//1 == 0:

        if year400/1 - year400//1 == 0:
            print( str(year) + " is a leap year")
    #If not divisible by 100 and 400 then check if year is divisible by 4
    elif year4/1 - year4//1 == 0:
        print( str(year) + " is a leap year")  
    #Else either something is wrong, or it is not a leap year.
    else:
        print( str(year) + " is not a leap year")

    

# Call our function
checkLeapYear()

# Define a variable to count how many times a the while loop has ran
repeats = 0

#Predicts the next 10 years, as to wether they are leap years or not
while repeats <= 9:
    repeatsYear = year + 1
    year = repeatsYear
    checkLeapYear()
    repeats = repeats + 1
