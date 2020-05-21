"""
My fourth lecture in python. Tuple and Dictionary
"""
#my_tuple = 'a', 'b', 'c', 'd', 'e'
#print(my_tuple[:])

#my_2nd_tuple = ('a', 'b', 'c', 'd', 'e')
#print(my_2nd_tuple)

#test = ('a',)
#print(type(test))

my_car = {
        'color': 'red',
        'make': 'toyota',
        'year': 2015
        }
        
#print(my_car['make'])
#print(my_car.get('year'))
#print(my_car.items())
#print(my_car.keys())
#print(my_car.values())
my_car['model'] = 'corolla'
my_car['year'] = 2020
print(my_car)
#print(len(my_car))
print('color' in my_car)