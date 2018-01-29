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

def is_dice(string):
    """validates dice string of form '^\d+d\d+\Z'
      ^ -- start of string
      \d -- digit
      + -- at least one (greedy)
      d -- char 'd'
      \Z -- end of string
    """
    regex = re.compile(r'^\d+d\d+\Z')
    return bool(regex.match(string))


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
ave = args.ave
M = args.M
L = args.L
S = args.S

err = "dice.py: Error: "
warn = "dice.py: Warning: "

# sanity checks
if not is_dice(dice):
    print(err + "'{0:s}' is not a valid dice string (i.e. '4d6')"
           .format(dice))
    exit()
if M<1:
    print(err + "cannot roll fewer than 1 trial")
    exit()
if M==1 and ave:
    print(warn + "computing average of 1 roll")
if L and S:
    print(err + "cannot keep both largest and smallest")
    print("  specify ONE of --large OR --small")
    exit()

N, D = map(int, dice.split('d'))

if L and L>=N:
    print(warn + "asked for largest {0:d} of {1:d} dice, keeping ALL"
           .format(L, N))
    L = None
if S and S>=N:
    print(warn + "asked for smallest {0:d} of {1:d} dice, keeping ALL"
           .format(S, N))
    S = None

# dice rolls, M trials of NdD
rolls = np.random.randint(D, size=(M, N)) + 1


sums = np.zeros(M, dtype=int)
if L:
    roll_name = "{0:s} keep largest {1:d}".format(dice, L)
    keep = np.argsort(rolls, axis=1)
    for mm, roll in enumerate(rolls):
        sums[mm] = np.sum( roll[keep[mm]][-L:] )
elif S:
    roll_name = "{0:s} keep smallest {1:d}".format(dice, S)
    keep = np.argsort(rolls, axis=1)
    for mm, roll in enumerate(rolls):
        sums[mm] = np.sum( roll[keep[mm]][:S] )
else:
    roll_name = "{0:s}".format(dice)
    sums = np.sum(rolls, axis=1)

if ave:
    print('ave of {0:s} x{1:d}'.format(dice, M))
    print('  {:f}'.format(np.mean(sums)))
else:
    print('{0:s} = '.format(roll_name))
    for mm, roll in enumerate(sums):
        print('  {:4d}'.format(roll))
