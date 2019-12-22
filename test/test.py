import unittest
import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi, fabs
from scipy import interpolate
from sympy import diff
from my_funct import sigma_observation, calman_filter, theory

def y(x):
    return x**2 + 1


print(diff(y(x))

class MyTestCase(unittest.TestCase):
    def test_sigma(self):
        test_x = []
        test_y = []
        sigma = 2.0
        epsilon = 0.05

        random.seed(888)

        count = 0
        while True:
            y = random.normalvariate(0, sigma)
            test_y.append(y)
            test_x.append(0.0)

            count += 1
            if count > 7000:
                break

        def zero(x):
            return 0.0

        test_model = theory(test_x, zero)

        new_sigma = sigma_observation(test_y, test_model)
        result = True
        if fabs(new_sigma - sigma) > epsilon:
            result = False

        self.assertTrue(result, " Ошибка в функции расчёта дисперсии ")


if __name__ == '__main__':
    unittest.main()
