#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:42:13 2024

@author: beesuut
"""

import numpy as np


def riemann(f, a, b, dx):
    return sum(f(i * dx + a) * dx for i in range(0, int((b - a) / dx)))


def f(x):
    return np.exp(-(x**2))


dx = 0.001
dy = 0.001

r = riemann(lambda y: riemann(f, y, 3, dy), 0, 3, dx)

print(f"Left Riemann Approximation for dx = {dx} and dy = {dy} is {r}")


def trapezoid(f, a, b, dx):
    return (
        sum(f(i * dx + a) for i in range(0, int((b - a) / dx)))
        - ((f(a) + f(b)) / 2)
    ) * dx


t = trapezoid(lambda y: trapezoid(f, y, 3, dy), 0, 3, dx)

print(f"Trapezoidal Approximation for dx = {dx} and dy = {dy} is {t}")
