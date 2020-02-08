# -------------------------------------------------------------------------------
# Name: Cyrus Ahmadi
# G#: 00973296
# Programming Assignment 2
# Due Date: 2/9/2020
# -------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
# -------------------------------------------------------------------------------
# References: (list resources used - remember, programming assignments are individual effort)
# -------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
# -------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
# 2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
# -------------------------------------------------------------------------------
from typing import Any


def intervals_relation(A_start, A_end, B_start, B_end):
    if (B_start <= A_start <= B_end) and (B_start <= A_end <= B_end):#This is if all numbers from set A fit into set B.
        result = 1
    elif (A_start <= B_start <= A_end) and (A_start <= B_end <= A_end):#This is if all numbers from set B fit into set A.
        result = 1
    elif (B_start <= A_start <= B_end) or (B_start <= A_end <= B_end):#This is if some numbers from set A fit into set B.
        result = -1
    elif (A_start <= B_start <= A_end) or (A_start <= B_end <= A_end):#This is if some numbers from set B fit into set A.
        result = -1
    else:
        result = 0#This is if no numbers fit into the other set.
    return result


# ------------------------------------------------------------------------------

def sphere_quadrant(x, y, z):
    if (x) ** 2 + (y) ** 2 + (z) ** 2 > 1:#formula to check if the point is in the unit circle.
        result = False
    elif (x >= 0 and x < 1) and (y >= 0 and y < 1) and (0 < z < 1):
        result = "green"
    elif (x >= 0 and x < 1) and (y >= 0 and y < 1) and (-1 < z <= 0):
        result = "lower green"
    elif (x >= 0 and x < 1) and (y > -1 and y < 0) and (0 < z < 1):
        result = "magenta"
    elif (x >= 0 and x < 1) and (y > -1 and y < 0) and (-1 < z <= 0):
        result = "lower magenta"
    elif (x > -1 and x < 0) and (y >= 0 and y < 1) and (0 < z < 1):
        result = "brown"
    elif (x > -1 and x < 0) and (y >= 0 and y < 1) and (-1 < z <= 0):
        result = "lower brown"
    elif (x > -1 and x < 0) and (y > -1 and y < 0) and (0 < z < 1):
        result = "blue"
    elif (x > -1 and x < 0) and (y > -1 and y < 0) and (-1 < z <= 0):
        result = "lower blue"
    else:
        result = False
    return result


# ------------------------------------------------------------------------------

def tile_fitting(num_small, num_large, length):
    if (5 * num_large) + num_small >= length and ((length / 5) <= num_small or (length / 5) == num_large or 5 * num_large + num_small == length):
        result = True#^formula to compute if the two numbers can fit evenly into the length.
    else:
        result = False

    return result

#
