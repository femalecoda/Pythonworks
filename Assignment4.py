#creat list called numbers 1,1,2,3,5,8,13,21,34,55,and 89
#write a program that print out all the element of the list that are less than 5

#empty_list = []
#numbers = list([1,1,2,3,5,8,13,21,34,55,89])
#for index in range(0,10):
 #   element = numbers[index]
 #   if element < 5:
 #       empty_list.append(element)



#print(empty_list)

#print(len(empty_list))

names = ["john","kay","lucy","john","mary","john","mark"]

matching_name = "john"
for items in range(0,7):
    recurring_name = names[items]
    if recurring_name == matching_name:
        print("john was found here")
