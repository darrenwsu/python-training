"""
nhap vao ten va tuoi
My name is {name}, {seconds} seconds.
"""
name = input("Enter your name: ")
age = int(input('age = '))

seconds = age * 365 * 24 * 60 * 60
print(f'My name is {name}, {seconds} seconds.')
