d1 = {'a' : 2, 'b' : 1, 'c' : 1}
d2 = {'a' : 3, 'b' : 1.1, 'd' : 2}
mylist = [d1, d2]
sum_dict = dict.fromkeys(set().union(*mylist), 0)

for d in mylist:
    for k in d.keys():
        sum_dict[k] += d[k]

print sum_dict

example_list = [
    {'points': 400, 'gold': 2480},
    {'points': 100, 'gold': 610},
    {'points': 100, 'gold': 620},
    {'points': 100, 'gold': 620}
]

# better memory
#print sum(item['gold'] for item in example_list)

# better time
#print sum([item['gold'] for item in example_list])

x = {'both1':1, 'both2':2, 'only_x': 100 }
y = {'both1':10, 'both2': 20, 'only_y':200, 'this':11 }

print {k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y) }


'''
A = {'a':1, 'b':2, 'c':3}
B = {'b':3, 'c':4, 'd':5}
c = {x: A.get(x, 0) + B.get(x, 0) for x in set(A).union(B)}

print(c)
'''

d1 = {'apples': 2, 'banana': 1}
d2 = {'apples': 3, 'banana': 2}
merged = reduce(
    lambda d, i: (
        d.update(((i[0], d.get(i[0], 0) + i[1]),)) or d
    ),
    d2.iteritems(),
    d1.copy(),
)

merged = dict(d1, **d2)
print merged