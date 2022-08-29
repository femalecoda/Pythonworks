     #WHILE LOOP IS USE WITH CONDITIONS(TRUE OR FALSE)
# 1. Ask user to enter password, if password is not correct
# say password incorrect , enter correct password.
# when user enter correct password
# print user password

# 2. Guessing Game
# Contunialy ask user for number, when user enters anumber
# tell the user if the number is even or odd number
# enter stop to end the program and print thank you for playing
# if the user enters three even numbers in a roll
# print you like even number and continue the loop enter numb


# A1
#user_password = True
#while user_password:
    #password = input("Enter password")
    #if password != "Gummy741" :
       # print("password incorrect")
    #else:
       # print(password#break

# A2
count = 0
user_number = True
while user_number:
    number = input("Please enter any number")
    if int(number) % 2 == 0:
        print("It's an even number")
        count = count + 1
        if count == 3 :
            print("you like even numbers")
            count = 0
    else:
        print(" The number is an odd number")
        break
print("Thank you for playing")



        
    
    


