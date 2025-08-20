import math
def cube_area(side):
    return 6 * side * side
def cube_volume(side):
    return side ** 3
def sphere_area(radius):
    return 4 * math.pi * radius ** 2
def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3
side = float(input("Enter the side length of the cube: "))
radius = float(input("Enter the radius of the sphere: "))
print(f"\nCube Surface Area: {cube_area(side):.2f}")
print(f"Cube Volume: {cube_volume(side):.2f}")
print(f"\nSphere Surface Area: {sphere_area(radius):.2f}")
print(f"Sphere Volume: {sphere_volume(radius):.2f}")