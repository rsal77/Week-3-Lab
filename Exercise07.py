# Promt user for colors
color1 = input('Enter the first color: ')
color2 = input('Enter the second color: ')

# Find out secondary colors from two primary colors

if (color1 == "red" and color2 == "blue") or (color1 == "blue" and color2 == "red"):
    print("Secondary color is Purple")
elif (color1 == "red" and color2 == "yellow") or (color1 == "yellow" and color2 == "red"):
    print("Secondary color is Orange")
elif (color1 == "blue" and color2 == "yellow") or (color1 == "yellow" and color2 == "blue"):
    print("Secondary color is Green")
else:
    print("You did not enter one of red, blue or yellow.")
