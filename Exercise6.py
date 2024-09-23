# Prompt user for date
month = int(input('Enter month in numeric form: '))
day = int(input('Enter day: '))
year = int(input('Enter two digit year: '))

# Find out if month times day equals year
if month * day == year:
    print('Date is magic.')
else:
    print('Date is not magic.')