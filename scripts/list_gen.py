# Imports random module
import random
# Imports PMCC function
from scipy.stats.stats import pearsonr


class ListGen:
    @classmethod
    def gen_list(cls, list_length):
        # Returns a random list of integers from 1 to 5
        return [random.randint(1, 5) for i in range(list_length)]

    @classmethod
    def calc_r(cls, list_x, list_y):
        # Returns pearson r of lists x and y
        return pearsonr(list_x, list_y)[0]

    @classmethod
    def gen_zero_r(cls):
        # Stores tries
        tries = 0
        while True:
            # Creates two lists of 12 integers from 1 to 5
            list_x = cls.gen_list(12)
            list_y = cls.gen_list(12)
            # Increments number of tries
            tries += 1
            if cls.calc_r(list_x, list_y) == 0:
                # Returns lists and tries if the two lists have zero r
                return list_x, list_y, tries
