#this program is to find out radius and circumference of a circle
import math
radius=float(input("Type the radius of the circle:"))
area= math.pi * (radius ** 2)
circumference=2 * math.pi *radius

print("The area of the circle is:",round(area))
print("The circumference of the circle is:",round(circumference))
