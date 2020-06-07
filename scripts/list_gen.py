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
        generated_zero = False
        while not generated_zero:
            list_x = cls.gen_list(12)
            list_y = cls.gen_list(12)
            if cls.calc_r(list_x, list_y) == 0:
                generated_zero = True
                return list_x, list_y
