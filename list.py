#create a list
list1 = [1, 2, 3, [1, 2, 3], 4, "I am arfan", 6.5]


#operations on list
list1.append(5)

#print(list1)

del(list1[7])

#print(list1)

#insert an element into a specific location
list1.insert(2, 10)

# print(list1)
# print(list1[3][0])
# print(list1[5])

#printing elements of list one by one using for loop
# for i in list1:
#     print("This is element: ",i)


#printing each element of list using while loop
# i = 2
# while list1[i] == 2:
#     print("This is correct sequence: ", list1[i])
#     i = i+1

#adding two lists
list2 = [1, 2, 3]
list3 = [4, 5, 6, 5]

print(list3+list2)
