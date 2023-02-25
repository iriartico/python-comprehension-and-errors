set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# Add
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# Update
set_countries.update({'bra', 'chi', 'arg', 'pe'})
print(set_countries)

# Remove
set_countries.remove('col')
# set_countries.remove('ar')
set_countries.discard('ar')
print(set_countries)

set_countries.clear()
print(set_countries)

