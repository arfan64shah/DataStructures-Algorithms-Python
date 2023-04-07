import array as arr

vals = arr.array('I', [1, 2, 3, 4, 5, 6, 7])
vals1 = arr.array('I', [6, 7, 8, 9, 0, 5])

#sum = vals + vals1

newarray = arr.array(vals.typecode, (a*a for a in vals))

# print(sum)
# for i in range(len(sum)):
#     print(sum[i])

i = 0
while i < len(newarray):
    print(newarray[i])
    i += 1
