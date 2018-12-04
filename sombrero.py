#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Grady Lynch and Frank Entriken
# Student ID: 2298368
# Email: grlynch@chapman.edu, entriken@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW12
###

import numpy as np
import numba as nb
import matplotlib.pyplot as plt

def RK4(F, y0, x0, N):
    x = np.zeros(N)
    y = np.zeros(N)

    x[0] = x0
    y[0] = y0

    t = np.linspace(0, (2*np.pi), N)

    d = (2 * np.pi)/N

    x1=0
    y1=0
    x2=0
    y2=0
    x3=0
    y3=0
    x4=0
    y4=0

    for i in range(1, len(t)):
        x1 = d*y[i]
        y1 = d*(-x[i]**3+x[i]-.25*y[i]+F*(np.cos(t[i])))

        x2 = d*(y[i] + y1/2)
        y2 = d*((-(x[i]+x1/2))**3+(x[i]+x1/2)-.25*(y[i]+y1/2)+F*(np.cos(t[i]+d/2)))

        x3 = d*(y[i]+y2/2)
        y3 = d*((-(x[i]+x2/2))**3+(x[i]+x2/2)-.25*(y[i]+y2/2)+F*(np.cos(t[i]+d/2)))

        x4 = d*(y[i]+y3)
        y4 = d*((-(x[i]+x3))**3+(x[i]+x3)-.25*(y[i]+y3)+F*(np.cos(t[i]+d)))

        x[i] = x[i-1] + (x1+2*x2+2*x3+x4)/6
        y[i] = y[i-1] + (y1+2*y2+2*y3+y4)/6


    plt.plot(x,y)
    return x
