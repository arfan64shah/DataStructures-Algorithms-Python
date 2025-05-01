# lists
mix_list = ['arfan', 'shah', 33, '03128865432', 'arfan@akdn.org']

# # for and if statements
# for i in mix_list:
#     if i == 33:
#         break
# print("The last element is age", i)

# # tuple
# my_tuple = (1, 'arfan', 3, 4, 5, 6, 7)
# print(my_tuple)

# # sets
# my_set = {1, 3, 2, 2, 2, 2, 7, 0, 10, 'name'}
# print(my_set)

# # array
# from array import array
# import numpy as np
# my_array = np.array([1, 2, 2, 1, 4])

# # perfomr an addition operation on my_array
# sum = 0
# for i in my_array:
#     sum = sum+i
# print("addition", sum)

# your_array = array('f', [1.11, 2.3])
# print(my_array)
# print(my_array.dtype)
# print(your_array)


# # dictionay
# my_dictionary = {
#     'first_name': 'arfan',
#     'second_name': 'shah',
#     'age': 25,
#     'phone': '03127765432'
# }
# print(my_dictionary['age'])
# print(my_array[1])
# print(mix_list[2])
# print(my_tuple[1])
# if 2 in my_set:
#     print("found")

# stack
stack = []

# add elements to stack
stack.append(0)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)

# remove element from stack
stack.pop()
print(stack)

from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)
queue.popleft()
print(queue)
