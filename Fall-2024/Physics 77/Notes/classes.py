# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:11:39 2024

@author: beesuut
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from my_timer import my_timer

# %% Subclasses and Inheritance


class soldier:
    def move(self):
        print("soldier is marching")


class naval_soldier(soldier):
    def move(self):  # Function overriding
        print("naval soldier is swimming")


def advance(p, n):
    assert isinstance(p, soldier)  # Python will accept naval_soldier
    for step in range(n):
        p.move()


finn = soldier()
alex = naval_soldier()

advance(finn, 3)
advance(alex, 4)
