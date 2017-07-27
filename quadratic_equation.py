from math import sqrt


def get_params():
    params = input('Enter the coefficients of the quadratic equation: ').split()
    try:
        params = list(map(float, params))
    except ValueError:
        print_error('Coefficients must be float')
        return None
    if len(params) != 3:
        print_error('There should be 3 coefficients ')
        return None
    return params


def print_error(error):
    print(error)


def get_roots(coef_1, coef_2, coef_3):
    discriminant = coef_2 ** 2 - 4 * coef_1 * coef_3
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return (-coef_2) / (2 * coef_1), None
    else:
        return (-coef_2 - sqrt(discriminant)) / (2 * coef_1), (-coef_2 + sqrt(discriminant)) / (2 * coef_1)


if __name__ == '__main__':
    params = get_params()
    if params:
        print(get_roots(*params))