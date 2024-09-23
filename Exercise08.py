# Prompt user number of people and number of hots dogs per person
people = int(input('Enter the number of people attending: '))
hotDogsPer = int(input('Enter the number of hot dogs each person should get: '))

# Hot dog variables
hotDogs = 10
buns = 8

# Calculate the number of hot dogs and buns needed
hotDogPgk = (people * hotDogsPer) // hotDogs
bunPgk = (people * hotDogsPer) // buns

totHotDogs = hotDogPgk
totBuns = bunPgk * buns

hotDogsLeft = (people * hotDogsPer) - totHotDogs
bunsLeft = (people * hotDogsPer) - totBuns

print(f'Total hot dogs {totHotDogs}')
print(hotDogsLeft)
print(bunsLeft)

print(hotDogPgk)
