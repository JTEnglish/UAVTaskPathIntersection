'''
 UAVTask.py:
    Class for collision avoidance for waypoint-based tasks

 Jacob English | je787413@ohio.edu
 2/26/19
'''

import math

'''
 Class: UAVTask
'''
class UAVTask:
    waypointLists = []
    altitude = 0
    speed = 0
    noflyZones = []

    '''
     UAVTask Function: __init__
        Parameters:
        Description:
    '''
    def __init__(self, waypoint_lists, altitude, speed, nofly_zones):
        self.waypointLists = waypoint_lists
        self.altitude = altitude
        self.speed = speed
        self.noflyZones = nofly_zones

    '''
     UAVTask Function: __lineIntersect
        Parameters:
        Description:
    '''
    def __lineIntersect(self, line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
           raise ValueError('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y

    def __distance(self, a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

    '''
     UAVTask Function: __isBetween
        Parameters:
        Description:
        Note: This function compares floating point numbers using
              math.isclose() and may have some precision issues for
              certain inputs.
    '''
    def __isBetween(self, pt0, intersect, pt1):
        distAB = self.__distance(pt0, intersect)
        distBC = self.__distance(intersect, pt1)
        distAC = self.__distance(pt0, pt1)

        # triangle inequality
        return math.isclose((distAB + distBC), distAC)

    #TODO: update to account for waypointLists
    def __timeAtPosition(self, wpt_index_before, position):
        t = 0
        for i in range(1, wpt_index_before + 1):
            d = self.__distance(self.waypointLists[0][i-1], self.waypointLists[0][i])
            t += d * (1 / self.speed)
        d = self.__distance(self.waypointLists[0][wpt_index_before], position)
        t += d * (1 / self.speed)
        return t


    '''
     UAVTask Function: __findIntersects
        Parameters:
        Description:
        Note: This function compares floating point numbers using
              math.isclose() and may have some precision issues for
              certain inputs.
    '''
    def __findIntersects(self, uavt_other):
        intersects = []
        for wpt_lst in self.waypointLists:
            for i in range(len(wpt_lst) - 1):
                self_line = [wpt_lst[i], wpt_lst[i+1]]
                # print('self line', self_line)
                for other_wpt_lst in uavt_other.waypointLists:
                    for j in range(len(other_wpt_lst) -1):
                        other_line = [other_wpt_lst[j], other_wpt_lst[j+1]]
                        # print('\tother line', other_line)
                        try:
                            point = self.__lineIntersect(self_line, other_line)

                            if (self.__isBetween(self_line[0], point, self_line[1]) and
                                self.__isBetween(other_line[0], point, other_line[1])):
                                print('\tPossible Intersection:', point)
                                time = self.__timeAtPosition(i, point)
                                if math.isclose(time, uavt_other.__timeAtPosition(j, point)):
                                    print('Intersection:', point, 'at t=', time)
                                    intersects.append((point, time))
                        except ValueError:
                            continue
        return intersects

    '''
     UAVTask Function: avoid
        Parameters:
        Description:
    '''
    def avoid(self, uavt_other):
        if type(uavt_other) is not UAVTask:
            raise ValueError('Function parameter must be of type UAVTask.')

        # get intersection points
        intersects = self.__findIntersects(uavt_other)

        return intersects ###STUB

        # check time vs position for intersection points
        # update task with zone avoidance
