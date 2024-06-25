# fruits = ['apple', 'oranges', 'banana']
# # print(fruits[0])

# # fruits[1] = "blueberry"
# # print(fruits)

# fruits.remove('apple')
# print(fruits)

# tuple
# fruits = ('apple', 'oranges')
# print(fruits)

# for fruit in fruits:
#     print(fruit)

# dictionary
person = {'name':'john', 'age':45, 'contact':"9920297423"}

person['age'] = 54
person['email'] = 'john@gmail.com'
del person['contact']

for key,value in person.items():
    print(f"{key} : {value}")
# print(person)