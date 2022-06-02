#Write a simple python program that adds 2 numbers together and output the result on your terminal.
#Your python program should use variables to carry out the addition

#Declaring the variables number_1 and number_2
number_1  = float(input("enter your first number: "))
number_2 = float(input("enter your second number: "))

#Function to return the addition of the two numbers
def add(a,b):
    return a + b


#implement the function to add two numbers
result = add(number_1, number_2)

#print the result in the terminal
print(result)

