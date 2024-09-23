# Prompt user for rectangle information

rectangle1_length = float(input('Input the length of rectangle 1: '))
rectangle1_width = float(input('Input the width of rectangle 1: '))

rectangle2_length = float(input('Input the length of rectangle 2: '))
rectangle2_width = float(input('Input the width of rectangle 2: '))

# Calculate area of rectangles

area1 = rectangle1_length * rectangle1_width
area2 = rectangle2_length * rectangle2_width

# Calculate which rectangle has greater area
if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area2 > area1:
    print('Rectangle 2 has the greater area.')
else:
    print('Both have the same area.')
