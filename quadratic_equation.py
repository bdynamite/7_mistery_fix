from math import sqrt


def get_params():
    params = input('Enter the coefficients of the quadratic equation: ').split()
    try:
        params = list(map(int, params))
    except ValueError:
        print('Coefficients must be integer')
        exit()
    if len(params) != 3:
        print('There should be 3 coefficients ')
        exit()
    return params


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return (-b) / (2 * a), None
    else:
        return (-b - sqrt(discriminant)) / (2 * a), (-b + sqrt(discriminant)) / (2 * a)


if __name__ == '__main__':
    params = get_params()
    print(get_roots(*params))   