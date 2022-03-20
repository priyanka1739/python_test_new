import math

def area(base, height):
    '''Return the area of the triangle '''
    return (base * height)/2


def perimeter(side1, side2, side3):
    '''Return the perimeter of the trianglee '''
    return side1 + side2+ side3


def semiperimeter(side1, side2, side3):
    '''Returns the semi perimeter of the triangle '''
    return perimeter(side1, side2, side3)/2

def area_new(side1, side2, side3):
    ''' Returns the squareroot '''

    semi = semiperimeter(side1, side2, side3)
    semi1 = semi * (semi-side1) * (semi-side2) * (semi-side3)

    return math.sqrt(semi1)


