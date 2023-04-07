import array as arr

vals = arr.array('I', [1, 2, 3, 4, 5, 6])
vals1 = arr.array('I', [6, 7, 8, 9, 0, 5])

sum = vals + vals1

print(sum)
for i in range(len(sum)):
    print(sum[i])

i = 0
while i < len(sum):
    print(sum[i])
    i += 1