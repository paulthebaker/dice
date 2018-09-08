#!/usr/bin/env python
"""dice.py
roll NdD dice
options:
    --large=L : only keep largest L dice: i.e. roll 4d6 keep largest 3 (char create)
    --small=S : only keep smallest S dice: i.e. roll 2d20 keep smallest S=1 (disadvantage)
    --repeat=M : repeat roll for M trials
    --average : compute average of trials
"""

from __future__ import (print_function, division)

import numpy as np
import argparse
import re

from dice import Dice

parser = argparse.ArgumentParser(description = 'simulated dice rolling!')

# options
parser.add_argument('dice', nargs=1,
                    action='store', type=str,
                    help="dice to roll as NdD (i.e. '4d6')")

parser.add_argument('-l','--large', dest='L',
                    action='store', type=int, default=None,
                    help='keep only the largest L dice')

parser.add_argument('-s','--small', dest='S',
                    action='store', type=int, default=None,
                    help='keep only the smallest S dice')

parser.add_argument('-r','--repeat', dest='M',
                    action='store', type=int, default=1,
                    help='repeat roll for M trials')

parser.add_argument('-a','--average', dest='ave',
                    action='store_true', default=False,
                    help='return average of M repeats')

args = parser.parse_args()

dice = args.dice[0]
M = args.M  # repeats
L = args.L  # largest
S = args.S  # smallest

err = "roll.py: Error: "
warn = "roll.py: Warning: "

myDice = Dice(args.dice[0], keep_large=L, keep_small=S)

if M<1:
    print(err + "cannot roll fewer than 1 trial")
    exit()
if M==1 and args.ave:
    print(warn + "computing average of 1 roll")

rolls = myDice.roll(num=M)

if L:
    roll_name = "{0:s} keep largest {1:d}".format(dice, L)
elif S:
    roll_name = "{0:s} keep smallest {1:d}".format(dice, S)
else:
    roll_name = "{0:s}".format(dice)
    
if args.ave:
    print('ave of {0:s} ({1:d} trials)'.format(roll_name, M))
    print('  {:f}'.format(np.mean(rolls)))
else:
    print('{0:s} = '.format(roll_name))
    for roll in rolls:
        print('  {:4d}'.format(roll))