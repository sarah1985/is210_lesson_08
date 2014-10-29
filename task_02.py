#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 08, Task 02 file"""


class Car(object):

    
    """A moving vehicle definition.

    Args:
        color (string): The color of the car. Defaults to ``'red'``.
        tires (list): Tires of the car. Defaults to None.

    Attributes:
       color (string): The color of the car.
       tires (list): Tires of the car.
    """

    def __init__(self, color='red', tires=None):
        self.color = color
        self.tires = tires
        if tires is None:
            tire_list = []
            tire_list.append(Tire())
            tire_list.append(Tire())
            tire_list.append(Tire())
            tire_list.append(Tire())
            self.tires = tire_list

class Tire(object):


    """A round rubber thing.

    Args:
        miles (integer): The number of miles on the Tire. Defaults to 0.

    Attributes:
       miles (integer): The number of miles on the Tire.
    """
    def __init__(self, miles=0):
        self.miles = miles
        self.__maximum_miles = 500

    def add_miles(self, miles):
        """Increments the tire mileage by the specified miles.

        Args:
            miles (integer): The number of miles to add to the tire.
        """
        self.miles += miles

    def get_maximum_miles(self):
        """get max miles"""
        return self.__maximum_miles

CAR_TEST = Car()
print CAR_TEST.tires

CAR_TEST2 = Car('blue', [Tire(100), Tire(100), Tire(200), Tire(200)])
print CAR_TEST2.tires