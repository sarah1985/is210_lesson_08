#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03: Create a Simple Class"""

import time


class Snapshot(object):
    """
    creating unix timestamp

    """
    def __init__(self):
        self.created = time.time()

SNAPSHOT = Snapshot()
print SNAPSHOT.created