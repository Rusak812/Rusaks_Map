import unittest
import numpy as np

from my_functions import average_population, Pareto
data_Foundation = np.genfromtxt("Foundation.data",names=True)
pop = data_Foundation['Population']

class MyTestCase(unittest.TestCase):

    def test_Pareto(self):
        self.assertTrue(Pareto(pop) > 0, " Ошибка в сортировки данных ")

    def test_Integ(self):
        temp = (average_population(pop) - np.trapz(pop))/average_population(pop)
        sigma = 1.3
        self.assertTrue(temp < sigma, " Плохой анализ интегралов ")

if __name__ == '__main__':
    unittest.main()
