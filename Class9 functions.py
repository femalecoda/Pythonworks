# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# function is repersented with def in python

def the_function(): # using the empty function method
    print("Hello, Mrs Odia")

the_function() # to call a function: use the function name followed by parenthesis

# Arguments (args): Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want, just separate them with a comma.

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# The following example has a function with one argument (fname).
#When the function is called, we pass along a first name, which is used inside the function to print the full name:

def my_name(fname):
    print(fname +" " + "Dave")

my_name("Crystal")# using the single parameter
my_name('David')
my_name("Olive")

          
def print_my_name(name_of_person): 
    print(f"your name is {name_of_person}") ##########################################################################


def join_fname_and_lname(firstname,lastname): # This function expects 2 parameters, and gets 2 arguments:
    print(f"{firstname} {lastname}")
    print_my_name(firstname)

def  add_numbers(number1,number2):
    result = number1 + number2
    join_fname_and_lname(number1,number2)
    return result     #To let a function return a value, use the return statement:

#result1 = add_numbers(20,8)
#print(result1)

#result2 = add_numbers("zainab","odia")
#print(result2)

# Create a calculator function that multiply,divde, subtract two number
#number1 = int(input("enter first number: "))
#number2 = int(input("enter second number: "))

 
def multiply_two_numb(number1,number2):
    result1 = number1 * number2
    return result1


def divide_two_numb(number1,number2):
    result2 = number1 + number2
    return result2


def subtract_two_numb(number1,number2):
    result3 = number1 - number2
    return result3

#result1 = multiply_two_numb(number1,number2)
#print(result1)

#result2 = divide_two_numb(number1,number2)
#print(result2)

#result3 = subtract_two_numb(number1,number2)
#print(result3)


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add an asterisk (*) before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def send_message(*message):
    print(f"sending {message[0]}")

send_message("welcome", "beginning", "tomorrow" )

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def send_receiver(receiver,times): # Key-value argument function
    print(f"sending to {receiver} at  {times}")

send_receiver(receiver = "07050503047", times = "7:30pm")

# Arbitrary Keyword Arguments, **kwargs
#If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def content_of_a_cabinet(**cabinet):
    print(cabinet["money"], cabinet["book"], cabinet["purse"])

content_of_a_cabinet(money = "300", book = "eze goes to school", purse = "key")

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def nationality(country = "canada"):
    print(f"I am from {country}")

nationality()
nationality("plymonth")
nationality("nigeria")
nationality("florida")

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

def staple(eat):
    for x in eat:
        print(x)
        
food = ["rice","bean","yam",]

staple(food)


# To let a function return a value, use the return statement:
# Example

def multiply_num(x):
  return 5 * x

print(multiply_num(4))
print(multiply_num(5))
print(multiply_num(7))       
          
# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.

#def my_function()
    pass # having an empty function definition like this, would raise an error without the pass statement

