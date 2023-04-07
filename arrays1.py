from array import *

n = int(input("Enter the length of an array: "))

arr = array('I', [])


for i in range(n):
    a = int(input("Enter value: "))
    arr.append(a)

print(arr)


b = int(input("Enter a number: "))

n = 0
for c in arr:
    if b == c:
        print(n)
        break
    else:
        n+=1
