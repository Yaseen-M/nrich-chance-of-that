# Imports random module
import random
# Imports PMCC function
from scipy.stats.stats import pearsonr


class ListGen:
    @classmethod
    def gen_list(cls, list_length):
        return [random.randint(1, 5) for i in range(list_length)]

    @classmethod
    def calc_r(cls, list_x, list_y):
        r = pearsonr(list_x, list_y)[0]
        return r

    @classmethod
    def gen_zero_r(cls):
        tries = 0
        while True:
            list_x = cls.gen_list(12)
            list_y = cls.gen_list(12)
            tries += 1
            if cls.calc_r(list_x, list_y) == 0:
                return list_x, list_y, tries
