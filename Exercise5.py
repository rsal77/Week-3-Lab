# Prompt user to enter objects mass
mass = float(input('Enter weight of object: '))

# Calculate mass and weight of object
weight = mass * 9.8

# Display message indicating about weight
if weight > 500:
    print('Too heavy')
elif weight < 100:
    print('Too light')

