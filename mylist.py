#creating an empty list
my_list = []

#append the values 10,20,30,40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert the value "15" to the 2nd position on the list
my_list.insert(1,15)

#extend my_list with another list
my_list.extend([50,60,70])

#remove the last last element from my_list
my_list.pop(-1)
#arrange list in ascending order
my_list.sort()

print (my_list)
#to find and print the index of y
y = my_list.index(30)
print(y)
