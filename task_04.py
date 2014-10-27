#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Subclassing"""

import task_02

class Tigerpaw(task_02.Tire):
    """override maximum miles"""

    def __init__(self, miles=0):
        self.miles = miles
        self.__maximum_miles = 750

CAR_TEST = task_02.Car()
print CAR_TEST.tires
