# Create four list
#use [] for the frist two list and list consturctor for the others
# List1 is a number of the first 6 months in a year
# List2 is a list of product in a supermarket that contains 10 items
# create a varaible that hold the sum of list1 and list2 and print
# list3 is a list of 10 floating point values
#use a for Loop to sum up every thing and print the total sum
# print the rang of value for -4 and -5 for list3


list_of_months = ["january","february","march","may","june","july"]
supermarket_list = ["cereal","milk","yogurt","yam","rice","bread","butter","honey","beans","nuts"]
sum_of_both_lists = list_of_months , supermarket_list
#print(sum_of_both_lists)

list_floats = list([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.9,0.10,0.11])
total_sum = 0
for index in range(0,10):
    item = list_floats[index]
    total_sum = item + total_sum
print("sum of items on list is:",total_sum)


#total = ""
#for index in range(0,10):
#    item = supermarket_list[index]
#    total = total +" " + item 
#print(total)



print(supermarket_list[2:-5:3])
print("test")








