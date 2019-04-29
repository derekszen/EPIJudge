from test_framework import generic_test
import math

# use recursive solution
# worst case runtime is O(n)
# n is number of bits in binary representation of y
def power(x: float, y: int) -> float:
    if(y == 1):
        return x
    return power(x*x, y>>1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
