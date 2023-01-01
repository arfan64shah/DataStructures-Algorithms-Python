dict = {'January': 2200, 'February': 2350, 'March': 2600, 'April': 2130, 'May': 2190}


difference = dict['February'] - dict['January']

print(difference)


sumOfThreeMonths = dict['January'] + dict['February'] + dict['March']

print(sumOfThreeMonths)

for i in dict:
    if(dict[i] == 2000):
        print("2000 is spent in ",i)
    else:
        print("2000 is not spent in ", i)
dict['June'] = 1980
dict['April'] = 1930

print(dict)