car_prices = {'Opel': 5000, 'Toyota': 7000, 'BMW': 10000}

print(car_prices)
print(car_prices['Opel'])

car_prices['Mazda'] = 4000
print(car_prices)

car_prices['Opel'] = 2500
print(car_prices)

del car_prices['Toyota']
print(car_prices)

# del car_prices
# print(car_prices)

car_prices.clear()
print(car_prices)


person = {
    'first name': 'Jack',
    'last name': 'Brown',
    'age': 43,
    'hobbies': ['football', 'singing', 'photo'],
    'childrens': {
        'son': 'Alex',
        'daugter': 'Ann'
    }
}

print(person)
print(person['age'])
print(person['hobbies'][0])
print(person['childrens']['son'])

person['car'] = 'Mazda'
print(person)

person['hobbies'][0] = 'basketball'
print(person['hobbies'][0])


print(person.keys())
print(person.values())
print(person.items())
