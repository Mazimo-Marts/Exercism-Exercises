def equilateral(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    return a == b == c


def isosceles(sides):
    a, b, c = sides    
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b >= c and b + c >= a and a + c >= b:
        return a == b != c or a != b == c or a == c != b or a == b == c
    return False


def scalene(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b >= c and b + c >= a and a + c >= b:
        return a != b and b != c and c != a
    return False
