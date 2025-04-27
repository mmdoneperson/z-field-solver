def prime(nubmer):  # функция, которая выводит все делители числа
    dividers = []
    divider = 1
    while divider * divider < abs(nubmer):
        if nubmer % divider == 0:
            dividers += [divider, nubmer // divider]
        divider += 1
    if divider * divider == abs(nubmer):
        dividers.append(divider)
    return dividers


def make_roots(dividers1, dividers2):  # функция, которая создает возможные корни
    possible_roots = []
    for p in dividers2:
        for q in dividers1:
            possible_roots += [p / q, -p / q]
    return possible_roots


def find_roots(possible_roots, coefficients):  # функция, которая проверяет, является ли число - корнем уравнения
    roots1 = []
    roots2 = []
    for x in set(possible_roots):  # реализация через схему Горнера
        while True:
            previous = coefficients[0]
            new_coefficients = [previous]
            for cf in coefficients[1:]:
                previous = x * previous + cf
                new_coefficients += [previous]
            if abs(previous) < 1e-9:
                roots2 += [x]
                if str(x)[-2:] == '.0':
                    x = int(x)
                if x > 0:
                    roots1.append(f'(x-{x})')
                elif x < 0:
                    roots1.append(f'(x+{-1 * x})')
                else:
                    roots1.append('x')
                coefficients = new_coefficients[:-1]
            else:
                break
    end = '('
    for i in range(len(coefficients)):
        if coefficients[i] == 0:
            continue
        cf = str(coefficients[i])
        if coefficients[i] > 0 and i != 0:
            cf = '+' + str(coefficients[i])
        if coefficients[i] == 1.0 or coefficients[i] == -1.0:
            if i != len(coefficients) - 1:
                cf = cf[0]
                if cf[0] == '1':
                    cf = ''
        if cf[-2:] == '.0':
            cf = cf[:-2]
        if i < len(coefficients) - 2:
            end += f'{cf}x^{len(coefficients) - i - 1}'
        elif i == len(coefficients) - 2:
            end += f'{cf}x'
        else:
            end += f'{cf}'
    end += ')'
    if len(coefficients) != 1:
        roots1.append(end)
    return roots1, roots2


def main(coefficients):  # функция, принимающая коэффициенты у уравнения
    a_n = coefficients[0]
    a_0 = coefficients[-1]
    dividers1 = prime(a_n)
    dividers2 = prime(a_0)
    possible_roots = make_roots(dividers1, dividers2)
    roots = find_roots(possible_roots, coefficients)
    print('Разложение:' + ''.join(roots[0]))
    print('Корни:', roots[1])
    return ''

print(main([1, 0 , -4])) # пример
