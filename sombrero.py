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

def RK4(x0, y0, F, N):
    x = np.zeros(N*50)
    y = np.zeros(N*50)

    x[0] = x0
    y[0] = y0

    t = np.linspace(0, (2*np.pi*50), N*50)
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
        x1 = d*y[i-1]
        y1 = d*((x[i-1])-(x[i-1])**3-(0.25*y[i-1])+(F*np.cos(t[i-1])))

        x2 = d*(y[i-1] + y1/2)
        y2 = d*((x[i-1]+x1/2)-(x[i-1]+x1/2)**3-(0.25*y[i-1]+y1/2)+(F*np.cos(t[i-1]+d/2)))

        x3 = d*(y[i-1]+y2/2)
        y3 = d*((x[i-1]+x2/2)-(x[i-1]+x2/2)**3-(0.25*y[i-1]+y2/2)+(F*np.cos(t[i-1]+d/2)))

        x4 = d*(y[i-1]+y3)
        y4 = d*((x[i-1]+x3)-(x[i-1]+x3)**3-(0.25*y[i-1]+y3)+(F*np.cos(t[i-1]+d)))

        x[i] = x[i-1] + (x1+2*x2+2*x3+x4)/6
        y[i] = y[i-1] + (y1+2*y2+2*y3+y4)/6

    plt.plot(t,x)
    plt.plot(t,y)
    plt.figure()
    plt.plot(x,y)
    plt.figure()

    xx = np.zeros(N*50)
    yy = np.zeros(N*50)
    for i in range (0,50):
        xx[i] = x[i*N]
        yy[i] = y[i*N]

    plt.scatter(xx,yy)

def RK4_2(x0, y0, F, N):
    x = np.zeros(N*1000)
    y = np.zeros(N*1000)

    x[0] = x0
    y[0] = y0

    t = np.linspace(0, (2*np.pi*50), N*1000)
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
        x1 = d*y[i-1]
        y1 = d*((x[i-1])-(x[i-1])**3-(0.25*y[i-1])+(F*np.cos(t[i-1])))

        x2 = d*(y[i-1] + y1/2)
        y2 = d*((x[i-1]+x1/2)-(x[i-1]+x1/2)**3-(0.25*y[i-1]+y1/2)+(F*np.cos(t[i-1]+d/2)))

        x3 = d*(y[i-1]+y2/2)
        y3 = d*((x[i-1]+x2/2)-(x[i-1]+x2/2)**3-(0.25*y[i-1]+y2/2)+(F*np.cos(t[i-1]+d/2)))

        x4 = d*(y[i-1]+y3)
        y4 = d*((x[i-1]+x3)-(x[i-1]+x3)**3-(0.25*y[i-1]+y3)+(F*np.cos(t[i-1]+d)))

        x[i] = x[i-1] + (x1+2*x2+2*x3+x4)/6
        y[i] = y[i-1] + (y1+2*y2+2*y3+y4)/6

    plt.plot(t,x)
    plt.plot(t,y)
    plt.figure()
    plt.plot(x,y)
    plt.figure()

    xx = np.zeros(N*1000)
    yy = np.zeros(N*1000)
    for i in range (0,1000):
        xx[i] = x[i*N]
        yy[i] = y[i*N]

    plt.scatter(xx,yy)