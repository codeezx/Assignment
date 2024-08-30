# PART 2 :-  BASIC PYTHON SYNTAX.
# 1. STRING OPERATION

# Write a Python program that takes a user's first and last name as input and print them in reverse order with a space between them.
first_name = input("Enter the first name:-  ")
last_name = input("Enter the last name:-  ")

reversed_name = last_name + " " + first_name
print(reversed_name)


# Use at least two string methods and explain their purpose in the comments.
'''
.capitalize() --->  This method in Python is used to capitalize the first character of a string and convert 
                    all other characters to lowercase. '''

text = input("Enter the string:-  ")
print(text.capitalize())

'''
.strip() --->  This method in Python is used to remove any leading and trailing whitespace (spaces, tabs, newlines) from a string.
               If no arguments are passed, it removes all types of leading and trailing whitespace. You can also specify characters 
               to remove by passing them as an argument. '''

text1 = "   Hello, World!   "
stripped_text = text1.strip()
print(stripped_text)



# 2. Numeric DataTypes and Conversion Functions

# Write a python program that take input from user, convert it to different numeric datatype(integer, float, complex) 
# and displays the converted value.

user_input = input("Enter the number:- ")

# Convert input it into integer.
int_value = int(user_input)         # int = It convert the user input into integer value.
print(type(int_value))

# Convert input into float.
float_value = float(user_input)    # float = It convert the user input into floating value.
print(type(float_value))

# Convert input into complex.
complex_value = complex(user_input)      # complex = It convert the user input into complex value.
print(type(complex_value))



# 3. Simple Input and Output
length = float(input("Enter the length of the rectangle:- "))
width = float(input("Enter the width of the rectangle:- "))

area = length * width
print("Area of rectangle is ", area)

# 4. Using fromat() function.
print("Area of rectangle is {:.2f}".format(area))



# 5. The % Method and Print function

# Write a Python Script that take three number as input and prints their average using the % method for string formatting.
num1=float(input("Enter the first value"))
num2=float(input("Enter the second value"))
num3=float(input("Enter the third value "))

average = (num1+num2+num3)/3

# Also, use the print function to display a message that states , "The average of the number is: [calculated average]".
print("The average of the three numbers is: %2f" % average)



# PART 3 :-  LANGUAGE COMPONENT
# 1. Control Flow (if Statements and Loops)

# Write a python program that asks the user for a number and determines wether it is positive, negative and zero.

num = int(input("Enter the number:- "))

if(num > 0):
    print("Positive")
elif( num < 0):
    print("Negative")
else:
    print("Zero")


# Implement a loop that continues to ask the user for a number until they enter 'exit'.
while True:
    user = input("Enter the number\n")
    
    if user == 'exit':
        print("Sayonara!")
        break
    
    
# Use break to exit the loop and continue to prompt for a new number if the input is not 'exit'.
while True:
    user_prompt = input("Enter the number\n")
    
    if user_prompt == 'exit':
        print("Sayonara!")
        break
    
    try:
        number = int(user_prompt)
        print("Number is ", number)
        
    except ValueError:
        print("Number is not valid! Try again")
        continue
    

# 2. Reational and Logical Operators

# Create a python script that takes two members as input and print wether both members are even, odd or one of 
# each using relational and logocal operator.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
    
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")

else:
    print("One number is even and the other is odd.")


# 3. For Loop and Bitwise Operator

# Write a python program that takes an integer input and prints its binary, octal and hexadecimal equivalents 
# using a for loop and bitwise operator.

num = int(input("Enter an integer: "))

# Define a dictionary to store the number bases and their respective formats
formats = {
    'Binary': 2,
    'Octal': 8,
    'Hexadecimal': 16
}
for base_name, base in formats.items():
    if base == 2:
        # Convert to binary using bitwise shift and mask
        binary = ""
        for i in range(num.bit_length() - 1, -1, -1):
            binary += str((num >> i) & 1)
        print(f"{base_name}: {binary}")
    elif base == 8:
        # Convert to octal using format function
        octal = format(num, 'o')
        print(f"{base_name}: {octal}")
    elif base == 16:
        # Convert to hexadecimal using format function
        hexadecimal = format(num, 'x').upper()
        print(f"{base_name}: {hexadecimal}")
