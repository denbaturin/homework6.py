my_dict = {'Denis': 1982, 'Taisiya': 2013, 'Savelii': 2009, 'Liliya': 1983}
print('Dict:', my_dict)

print('Existing value: ', my_dict['Savelii'])

print('Not existing value: ', my_dict.get('Nikodim'))

my_dict.update({'Mama': 1956, 'Papa': 1952})

print('Deleted value: ', my_dict.pop('Denis'))
print('Modified dictionary: :', my_dict)

print()

my_set = {1,2,3,1,2,3, 'Denis', False, 'Denis', False}
print('Set: ', my_set)
my_set.update([88, 'Inokentii',(9,8,7)])
my_set.discard(False)

print('Modified set: ', my_set)