"""
Math:
    math.prod - return the product of the numerical containers.
    math.isqrt - return the integral part of the root of the number.
    math.dist - return the distance between the two points. 3D or 2D.
    math.hypot - return the hypotenuse of a right angle triangle.

Statistics:
    statistics.fmean - return the arithmetic mean of a sequence of numbers.
    statistics.geometric_mean - return the geometric median of a sequence of numbers.
    statistics.multimode - return the most frequently sequential number.


"""

# Example_1 math.prod ----------------------------------------------------------------
import math

nums_v1 = [2, 3, 6, 8]  # numeric container.
nums_v2 = (2, 3, 6, 8)  # numeric container.
nums_v3 = {2, 3, 6, 8}  # numeric container.
# 2 * 3 * 6 * 8
print(math.prod(nums_v1))
print(math.prod(nums_v2))
print(math.prod(nums_v3))

# Example_2 math.isqrt ----------------------------------------------------------------

print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(17))
print(math.sqrt(17))

# Example_3 math.dist ----------------------------------------------------------------

p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))

# Example_4 math.hypo ----------------------------------------------------------------

print(math.hypot(*p3d1))  # The * remove the elements from the list.
print(math.hypot(*p2d1))

# Example_5 statistics.fmean ----------------------------------------------------------------

import statistics

real_values = [1.45, 6.78, 3.45, 89.98]
integer_values = [1, 6, 3, 89]

print(statistics.fmean(real_values))  # real median
print(statistics.fmean(integer_values))  # real median

# Example_6 statistics.multimode ----------------------------------------------------------------

seq1 = 'NameNameMultiName'
seq2 = [3, 5, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
