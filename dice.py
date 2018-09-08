# dice.py
"""utilities for dice"""

from __future__ import (print_function, division)

import numpy as np
import re

def _is_dice(string):
    """validates dice string of form '^\d+d\d+\Z'
      ^ -- start of string
      \d -- digit
      + -- at least one (greedy)
      d -- char 'd'
      \Z -- end of string
    """
    regex = re.compile(r'^\d+d\d+\Z')
    return bool(regex.match(string))

class Dice(object):
    """class for dice"""
    def __init__(self, dice, keep_large=None, keep_small=None):
        """instantiate dice object
        
        :param dice: string
            Dice string of the form NdD, where N is the number of dice
            and D is the size of dice (e.g. '4d6').
        :param keep_large: int
            only keep largest L rolls.  For example in D&D character gen
            ``dice = '4d6', keep_large = 3``.
        :param keep_small: int
            only keep smallest S rolls.  For example in D&D 5e disadvantage
            ``dice = '2d20', keep_small = 1``
        
        You cannot specify both ``keep_small`` and ``keep_large`` in the same
        instance.
        """
        if not _is_dice(dice):
            msg = "'{0:s}' is not a valid dice string (e.g. '4d6')".format(dice)
            raise ValueError(msg)
        if keep_large and keep_small:
            msg = ("cannot keep both largest and smallest rolls",
                    "specify ONE of keep_large or keep_small")
            raise ValueError(msg)

        self._dice = dice
        self._large = keep_large
        self._small = keep_small
        self._N, self._D = map(int, dice.split('d'))

        if self._large and self._large >= self._N:
            warn = ("WARNING: asked for largest {0:d} of {1:d} dice, keeping ALL"
                    .format(self._large, self._N))
            print(warn)
            self.large = None
        if self._small and self._small >= self._N:
            warn = ("WARNING: asked for smallest {0:d} of {1:d} dice, keeping ALL"
                    .format(self._small, self._N))
            print(warn)
            self._small = None

    @property
    def dice():
        return self._dice
    @property
    def N():
        return self._N
    @property
    def D():
        return self._D
    @property
    def large():
        return self._large
    @property
    def small():
        return self._small

    def roll(self, num=1):
        """roll dice
        :param num: int
            number of rolls
        """
        rolls = np.random.randint(self._D, size=(num, self._N)) + 1
        rank = np.argsort(rolls, axis=1)

        if self._large:
            tots = np.sum([roll[ss][-self._large:] for roll,ss in zip(rolls,rank)],
                          axis=1)
        elif self._small:
            tots = np.sum([roll[ss][:self._small] for roll,ss in zip(rolls,rank)],
                          axis=1)
        else:
            tots = np.sum(rolls, axis=1)

        return tots