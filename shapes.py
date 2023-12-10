# # Calculating Areas of Shapes:

# # Area of rectangle: 
# print("Area of rectangle:")
# rectangle_length = int(input("Enter the length of the rectangle: "))
# rectangle_breadth = int(input("Enter the breadth of the rectangle: "))
# rectangle_area = float(rectangle_length * rectangle_breadth)
# print(f"The area of the rectangle with lenghth {rectangle_length:.1f} and breadth {rectangle_breadth:.1f} is: {rectangle_area:.2f}")
# print("")

# # Perimeter of rectangle:
# print("Perimeter of rectangle:")
# rectangle_length = int(input("Enter the length of the rectangle: "))
# rectangle_breadth = int(input("Enter the breadth of the rectangle: "))
# rectangle_perimeter = float(2 * (rectangle_length + rectangle_breadth))
# print(f"The perimeter of the rectangle with lenghth {rectangle_length:.1f} and breadth {rectangle_breadth:.1f} is: {rectangle_perimeter:.2f}")
# print("")

# # Area of triangle:
# print("Area of triangle:")
# triangle_base = int(input("Enter the base of the triangle: "))
# triangle_height = int(input("Enter the height of the triangle: "))
# triangle_area = float((triangle_base * triangle_height) * 0.5)
# print(f"The area of triangle with base {triangle_base:.1f} and height {triangle_height:.1f} is: {triangle_area:.2f}")
# print("")

# # Perimeter of triangle:
# print("Perimeter of triangle:")
# triangle_base = int(input("Enter the base of the triangle: "))
# triangle_height = int(input("Enter the height of the triangle: "))
# triangle_width = int(input("Enter the width of triangle: "))
# triangle_perimter = float(triangle_base + triangle_height + triangle_width)
# print(f"The area of triangle with base {triangle_base:.1f} and height {triangle_height:.1f} and width {triangle_width:.1f} is: {triangle_perimter:.2f}")
# print("")

import math

# # Area of cirlce: 
# print("Area of circle:")
# cricle_radius = int(input("Enter the radius of circle: "))
# circle_area = float(math.pi * cricle_radius ** 2)
# print(f"The area of the circle with radius {cricle_radius:.1f} is: {circle_area:.2f}")
# print("")

# # Perimeter of cirlce: 
# print("Perimeer of circle:")
# cricle_radius = int(input("Enter the radius of circle: "))
# circle_perimeter = float(2 * math.pi * cricle_radius)
# print(f"The area of the circle with radius {cricle_radius:.1f} is: {circle_perimeter:.2f}")
# print("")

def triangle_area(base, height):
    return (base * height) * 0,5

def rectangle_area(lenght, breadth):
    return lenght * breadth

def circle_area(radius):
    return math.pi * radius ** 2

def square_perimeter(side_length):
    return 4 * side_length

def circle_details(radius):
    circumference = radius * math.pi * 2
    area = math.pi * radius ** 2
    print(f"Circumference: {circumference}")
    print(f"Area: {area}")
    return circumference, area

def geometry(square_side, circle_radius):
    square_perim = square_perimeter(square_side)
    circle_circumference, _ = circle_details(circle_radius)
    square_area = square_side ** 2
    circle_area_value = circle_area(circle_radius)

    if square_perim > circle_circumference:
        print("Square has a larger perimeter.")
    elif square_perim == circle_circumference:
        print("The two shapes have equal perimeters.")
    else:
        print("Circle has a larger circumference.")

    if square_area > circle_area_value:
        print("Square has a larger area.")
    elif square_area == circle_area_value:
        print("The two shapes have equal area.")
    else:
        print("Circle has a larger area.")

square_side = 17
circle_radius = 7

geometry(square_side, circle_radius)
