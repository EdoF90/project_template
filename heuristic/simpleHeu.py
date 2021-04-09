# -*- coding: utf-8 -*-
import time
import math
import logging

class SimpleHeu():
    def __init__(self, n):
        self.n = n

    def solve(
        self, dict_data
    ):
        sol_x = [0] * dict_data['n_items']
        start = time.time()
        sol_x[self.n] = math.ceil(dict_data['max_size'] / dict_data['sizes'][0])
        end = time.time()
        
        of = dict_data['profits'][self.n] * sol_x[self.n]
        comp_time = end - start
        
        return of, sol_x, comp_time
