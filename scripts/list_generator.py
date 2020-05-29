# Imports random module
import random
# Imports PMCC function
from scipy.stats.stats import pearsonr


def generate_list(list_length):
    return [random.randint(1, 5) for i in range(list_length)]


def get_pearsonr(list_x, list_y):
    r = pearsonr(list_x, list_y)[0]
    return r


def generate_zero_r():
    generated_zero = False
    while not generated_zero:
        list_x = generate_list(12)
        list_y = generate_list(12)
        if get_pearsonr(list_x, list_y) == 0:
            generated_zero = True
            return list_x, list_y


def main():
    lists = generate_zero_r()
    list_x = lists[0]
    list_y = lists[1]
    print("List x: " + str(list_x))
    print("List y: " + str(list_y))


main()
