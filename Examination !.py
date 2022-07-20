# 1. Declare a variables caled number of days, with int 30
# 2. Declare a variable is amount complete, set it to boolen True
# 3. Declare a varable Lenght of sides, set to Float 200.07
# 4. Declare a varible header title, set to string welcome to nigeria
# 5. Declare a varible total sum, set it to (int in Q1 "30 raise to power 2"
# 6. Declare a varible Result for today, set it to the (float in Q3 " 200.07 multiple by 5"
# 7. Declare a varible the sum, set it to 15 + 16
# 8. Declare a varible the product set it to 7*17
# 9. Declare three varaibe X 9,Y 18, Z 36
#10. create an if statement to print condition is true
#11. Inside the if condition check if x<y or y<z or x<z and the print statement must print
#12. Decale two varible set to passage1 set to sandra and passage2 janet
#13. write an if and else statment (If passage1 in bus print(sandra in the bus) elif print janet)
#14. creat a for loop print 11times starting from 1 - 100
#15. create a while loop asking user to Enter a number( when user enter number larger than 1millon print (program has terminated )


number_of_days = 30
a = 2
b = 5
is_amount_complete = True
lenght_of_sides = 200.07
header_title = "welcome to nigera"

total_sum = number_of_days ** a
print(total_sum)

result_for_today = lenght_of_sides * b
print(result_for_today)


number1 = 15
number2 = 16
the_sum = number1 + number2
print(the_sum)

number3 = 7
number4 = 17
the_product = number3 * number4
print(the_product)

x = 9
y = 18
z = 36
if (x < y) or (y < z) or (x < z):
    print("condition is true")

passager1 = "sandra"
passager2 = "janet"
if passager1 == "sandra":
    print("sandra in the bus")
elif passager2 == "janet":
    print("janet in the bus")
        

for number in range (0,101):
    if number >= 1:
        print("Eleven times ",number,"is", 11 * number)


        

number_million = True
while number_million:
    user = input("enter number")
    amount = 1000000
    if amount == int(user):
       print("program has terminated")
       number_million = False
       ss
    

