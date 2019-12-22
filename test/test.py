import unittest
import numpy as np

from my_functions import average_population, Pareto

class MyTestCase(unittest.TestCase):
    def test_Pareto(self):
        if (Pareto(pop) < 0):
            result = True
        else:
            result = False
        self.assertTrue(result, " Ошибка в сортировки данных ")

    def test_Integ(self):
        temp = (average_population(pop) - np.trapz(pop))/average_population(pop)
        sigma = 0.3
        if (temp > sigma):
            result = True
        else:
            result = False
        self.assertTrue(result, " Плохой анализ интегралов ")

if __name__ == '__main__':
    unittest.main()
