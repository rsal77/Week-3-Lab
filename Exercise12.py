# Prompt user for number of packages purchased
pkgPur = int(input('Enter number of packages: '))

# Package price variable
pkgPrice = 99


# Calculate discount

if pkgPur >= 10 and pkgPur <= 19:
    discount = 0.10
    print('Discount 10%')
elif pkgPur >=20 and pkgPur <= 49:
    discount = 0.20
    print('Discount 20%')
elif pkgPur >=50 and pkgPur <= 99:
    discount = 0.30
    print('Discount 30%')
elif pkgPur >= 100:
    discount = 0.40
    print('Discount 40%')

sale = (pkgPur * pkgPrice) * discount
total = (pkgPur * pkgPrice) - sale

print(f'Total amount is {total:,.2f}')