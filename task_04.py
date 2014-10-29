#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Subclassing"""

import task_02


class Tigerpaw(task_02.Tire):
    """override maximum miles"""

    def __init__(self, miles=0):
        super(Tigerpaw, self).__init__()
        self.miles = miles
        self.__maximum_miles = 750

    def get_maximum_miles(self):
        return self.__maximum_miles

if __name__ == "__main__":
    TEST = Tigerpaw()
    print TEST.get_maximum_miles()

    TEST2 = task_02.Tire()
    print TEST2.get_maximum_miles()