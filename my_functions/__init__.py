import numpy as np
import matplotlib.pyplot as plt

def average_population(pop):
    """Вычисление суммарного населения
    :pop:   список населения
    """
    print(np.trapz(pop))
    return np.sum(pop)

def Pareto(pop):
    """Вычисление индекса Парето
    :pop:   список населения
    """
    pop1 = pop
    pop1.sort()
    pop2 = pop1
    i = 0
    for _ in pop1:
        pop2[i] = pop1[-i]
        i += 1
    i = 1
    for _ in pop1:
        plt.scatter(i, np.log(pop1[-i]))
        i +=1
    plt.title('Pareto distribution of population')
    plt.xlabel('city index')
    plt.axis([0, 34.5, np.log(100), np.log(2500)])
    plt.ylabel('log of population')
    #plt.show()
    plt.clf()
    n = 34
    a = np.linspace(1, n, n)
    b = np.polyfit(a, np.log(pop1), 1)
    return b[0]


