#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt

from UAVTask import UAVTask

Xs = np.arange(0, 30, 0.2)
sinYs = [math.sin(x) for x in Xs]
neg_sinYs = [-y for y in sinYs]

uav0_pts = [(Xs[i], sinYs[i]) for i in range(len(Xs))]
uav1_pts = [(Xs[i], neg_sinYs[i]) for i in range(len(Xs))]

uav0 = UAVTask([uav0_pts], 100, 1, [])
uav1 = UAVTask([uav1_pts], 100, 1, [])

intersects = uav0.avoid(uav1)

plt.plot(Xs, sinYs, 'g', label='UAV 0')
plt.annotate(
    "UAV 0 Start",
    xy=(Xs[0], sinYs[0]), xytext=(5, -30),
    textcoords='offset points', ha='right', va='bottom',
    bbox=dict(boxstyle='round,pad=0.5', fc='green', alpha=0.5),
    arrowprops=dict(arrowstyle = '-', connectionstyle='arc3,rad=0'))

plt.plot(Xs, neg_sinYs, 'b', label='UAV 1')
plt.annotate(
    "UAV 1 Start",
    xy=(Xs[0], neg_sinYs[0]), xytext=(-30, 5),
    textcoords='offset points', ha='right', va='bottom',
    bbox=dict(boxstyle='round,pad=0.5', fc='blue', alpha=0.5),
    arrowprops=dict(arrowstyle = '-', connectionstyle='arc3,rad=0'))

for pt in intersects:
    plt.plot(pt[0][0], pt[0][1], marker='o', markersize=6, color="red")
    label = "t: " + "{:.5f}".format(pt[1])
    plt.annotate(
        label,
        xy=(pt[0][0], pt[0][1]), xytext=(0, 30),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
        arrowprops=dict(arrowstyle = '-', connectionstyle='arc3,rad=0'))

plt.xlim(-5, 40)
plt.grid(linestyle='-', linewidth=0.5)
plt.legend()
plt.show()
