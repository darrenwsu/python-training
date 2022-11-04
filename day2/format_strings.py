# name
name = 'Khanh'
print(name)

name = "Jack"

greeting = "My name is {}"

# My name is {name}
welcome = f'My name is {name}'
print(welcome)

name = "Kenny"
print(greeting.format(name))

name = 'Darren'
print(greeting.format(name))

# age
age = 22
print(age)

# My name is {name}. I am {age}.
# aaa = ' I am {}.'
# print(aaa)
# print(greeting.format(name), aaa.format(age), sep='.')

greeting = "My name is {}. I am {}. {}"
print(greeting.format(name, age, 2002))
