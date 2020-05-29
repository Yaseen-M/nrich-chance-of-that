# Imports random module
import random
# Imports PMCC function
from scipy.stats.stats import pearsonr


def generate_list(list_length):
    return [random.randint(1, 5) for i in range(list_length)]


def calc_r(list_x, list_y):
    r = pearsonr(list_x, list_y)[0]
    return r


def generate_zero_r():
    generated_zero = False
    while not generated_zero:
        list_x = generate_list(12)
        list_y = generate_list(12)
        if calc_r(list_x, list_y) == 0:
            generated_zero = True
            return list_x, list_y


def print_list(letter, output_list):
    print('List {}: {}'.format(letter, output_list))


def main():
    list_x, list_y = generate_zero_r()
    print_list('x', list_x)
    print_list('y', list_y)


main()
