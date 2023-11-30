
'''
   Description: Area of a triangle
   Output: See Below
   Known bugs: none
'''

import math

X1, Y1, X2, Y2, X3, Y3 = map(float, input("Enter the three coordinates for a triangle").split(","))
Side1 = math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
Side2 = math.sqrt((X3-X2)**2 + (Y3-Y2)**2)
Side3 = math.sqrt((X1-X3)**2 + (Y1-Y3)**2)

S = (Side1 + Side2 + Side3)/2
area = math.sqrt(S*(S-Side1)*(S-Side2)*(S-Side3))
print(" The area of the triangle is " + str(area))

'''
Output

 Enter the three coordinates for a triangle 1.5, -3.4, 4.6, 5, 9.5, -3.4
 The area of the triangle is 33.600000000000016
 
 Enter the three coordinates for a triangle 6, 6, 6, 6, 6, 6
 The area of the triangle is 0.0

'''










