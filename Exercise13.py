# Prompt user for weight of package
weight = float(input('Enter weight: '))

if weight <= 2:
    rpp = 1.50
elif weight > 2 and weight < 6:
    rpp = 3.00
elif weight > 6 and weight <= 10:
    rpp = 4.00
elif weight > 10:
    rpp = 4.75

shipping = weight * rpp

print(f'Shipping charge is {shipping:,.2f}')