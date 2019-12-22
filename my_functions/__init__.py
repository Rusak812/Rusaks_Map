from math import sqrt, fabs
import numpy as np
import matplotlib.pyplot as plt

def average_population(pop):
    """Вычисление дисперсии
    :pop:   список населения
    """
    print(np.trapz(pop))
    return np.sum(pop)

def Pareto(pop):
    """Вычисление дисперсии
    :pop:   список населения
    """
    pop1 = pop
    pop1.sort()
    #pop1.reverse()
    i = 1
    for _ in pop1:
        plt.scatter(i, np.log(pop1[-i]))
        i +=1
    plt.title('Pareto distribution of population')
    plt.xlabel('city index')
    plt.axis([0, 34.5, np.log(100), np.log(2500)])
    plt.ylabel('log of population')
    #plt.gca().invert_xaxis()
    plt.show()
    plt.clf()
    return 1


def k_cal(s_obs, s_mod):
    """Вычисление коэффициента фильтра Калмана
    :param s_obs:   среднеквадратическое отклонение измерений
    :param s_mod:   среднеквадратическое отклонение модели
    :return:        Коэффициент Калмана
    """
    sigma_obs2 = s_obs * s_obs
    sigma_mod2 = s_mod * s_mod
    e = sigma_obs2
    k = 1.0
    while True:
        mem_k = k
        e = sigma_obs2 * (e + sigma_mod2) / (e + sigma_obs2 + sigma_mod2)
        k = e / sigma_obs2
        if sqrt((k - mem_k) * (k - mem_k)) < 0.0000001:
            break
    return k


def calman_filter(x_obs, y_obs, model, sigma_obs, sigma_mod):
    """Фильтр Калмана
    :param x_obs:       список x - координаты измерений
    :param y_obs:       список y - координаты измерений
    :param model:       список модели измерений
    :param sigma_obs:   среднеквадратическое отклонение измерений
    :param sigma_mod:   среднеквадратическое отклонение модели
    :return:            список с отфильтрованными измерениями
    """
    filter_obs = []

    k = k_cal(sigma_obs, sigma_mod)

    x0 = model[0]
    filter_obs.append(x0)

    for i in range(1, len(x_obs)):
        x0 = k * y_obs[i] + (1.0 - k) * (x0 + model[i] - model[i-1])
        filter_obs.append(x0)

    return filter_obs


def filter_data(sub1, sub2, m1, m2, m3, sigma):
    """Фильтрация ложных измерений
    Вычисляется разница между измерениями и моделью,
    если она больше среднеквадратическое отклонения, то данное измерение
    удаляется из измерений и модели, а также из всех списков для фильтрации
    :param sub1:    список измерений
    :param sub2:    список модели
    :param m1:      список для фильтрации
    :param m2:      список для фильтрации
    :param m3:      список для фильтрации
    :param sigma:   среднеквадратическое отклонение измерений
    :return:
    """
    length = len(sub1)
    i = 0
    while i < length:
        if fabs(sub1[i] - sub2[i]) > sigma:
            del sub1[i]
            del sub2[i]
            del m1[i]
            del m2[i]
            del m3[i]
            length -= 1
        else:
            i += 1


def theory(x_obs, theoretical_function):
    """Формирование списка модели
    :param x_obs:                   список x - координаты измерений
    :param theoretical_function:    теоретическая функция модели
    :return:                        список со значениями теоретической функции модели в х-измерениях
    """
    result = []
    for i in range(0, len(x_obs)):
        result.append(theoretical_function(x_obs[i]))
    return result
