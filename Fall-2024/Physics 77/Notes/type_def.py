# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:16:12 2024

@author: beesuut
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% Type Def


def factorial(n: int) -> int:  # Type hint (for user & compiler)
    assert type(n) is int  # Type checking (forces variable type)
    if n == 0:
        return 1
    return n * factorial(n - 1)


# %% Polymorphism


def mult_by_3(n: int) -> int:
    return n * 3


def mult_by_3(s: str) -> str:  # Function overloading
    return f"{s}{s}{s}"
