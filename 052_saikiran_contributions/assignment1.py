operation = input('''
Please type the operations you would like to complete:
+ for addition
* for multiplication
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
number_3 = int(input('Enter your third number: '))
number_4 = int(input('Enter your fourth number: '))
print('{} + {} = '.format(number_1,number_2,number_3,number_4))
print(number_1 + number_2 + number_3 + number_4)
print('{} * {} = '.format(number_1,number_2,number_3,number_4))
print(number_1 * number_2 *number_3*number_4)

