# Prompt user for age
age = int(input('Please enter your age: '))

# Find out if user is an infant, child, teen or adult
if age <= 1:
    print('Infant')
elif age > 1 and age < 13:
    print('Child')
elif age >= 13 and age < 20:
    print('Teen')
elif age >= 20:
    print('Adult')