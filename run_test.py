#!/usr/bin/env python3

import json
import matplotlib.pyplot as plt

from UAVTask import UAVTask

def main():
    # Load UAV data from json files
    uav0_file = 'test_data/uav0_multiSegment.json'
    uav0_data = {}
    with open(uav0_file) as f:
        uav0_data = json.load(f)
    uav0 = UAVTask(uav0_data['waypointLists'],
                   uav0_data['altitude'],
                   uav0_data['speed'],
                   uav0_data['noflyZones'])
    print(uav0.__dict__)

    uav1_file = 'test_data/uav1_multiSegment.json'
    uav1_data = {}
    with open(uav1_file) as f:
        uav1_data = json.load(f)
    uav1 = UAVTask(uav1_data['waypointLists'],
                   uav1_data['altitude'],
                   uav1_data['speed'],
                   uav1_data['noflyZones'])
    print(uav1.__dict__)

    # Run uav0 avoidance function
    intersects = uav0.avoid(uav1) # current stub outputs line intersections

    # Graph
    uav0_Xs = [pt[0] for pt in uav0.waypointLists[0]]
    uav0_Ys = [pt[1] for pt in uav0.waypointLists[0]]
    plt.plot(uav0_Xs, uav0_Ys, 'g', label='UAV 0')
    plt.annotate(
        "UAV 0 Start",
        xy=(uav0_Xs[0], uav0_Ys[0]), xytext=(5, -30),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='green', alpha=0.5),
        arrowprops=dict(arrowstyle = '-', connectionstyle='arc3,rad=0'))

    uav1_Xs = [pt[0] for pt in uav1.waypointLists[0]]
    uav1_Ys = [pt[1] for pt in uav1.waypointLists[0]]
    plt.plot(uav1_Xs, uav1_Ys, 'b', label='UAV 1')
    plt.annotate(
        "UAV 1 Start",
        xy=(uav1_Xs[0], uav1_Ys[0]), xytext=(5, -30),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', fc='blue', alpha=0.5),
        arrowprops=dict(arrowstyle = '-', connectionstyle='arc3,rad=0'))

    for pt in intersects:
        plt.plot(pt[0][0], pt[0][1], marker='o', markersize=6, color="red")
        label = "t: " + "{:.5f}".format(pt[1])
        plt.annotate(
            label,
            xy=(pt[0][0], pt[0][1]), xytext=(-30, 5),
            textcoords='offset points', ha='right', va='bottom',
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '-', connectionstyle='arc3,rad=0'))

    plt.ylim(-10, 5)
    plt.grid(linestyle='-', linewidth=0.5)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
