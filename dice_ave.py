#!/usr/bin/env python
"""dice_ave.py
compute brute-force average outcome of 3 atypical, but useful dice rolls
TODO: generalize, take command line inputs
"""

from __future__ import (print_function, division)

import numpy as np

# roll 4d6, keep best 3
rolls = np.array([ [w+1, x+1, y+1, z+1] 
                    for w in range(6)
                    for x in range(6) 
                    for y in range(6) 
                    for z in range(6) ])

outcome = np.sum(rolls, axis=1) - np.min(rolls, axis=1)
ave_4d6 = np.mean(outcome)

print("4d6, keep 3 ave: {0}".format(ave_4d6))

# roll 2d20, keep best or worst 1
rolls = np.array([ [x+1, y+1] 
                    for x in range(20) 
                    for y in range(20) ])

adv = np.max(rolls, axis=1)
dis = np.min(rolls, axis=1)

ave_adv = np.mean(adv)
ave_dis = np.mean(dis)
ave_d20 = 10.5

adv = ave_adv - ave_d20
dis = ave_dis - ave_d20

print("d20 with advantage ave: {0},  i.e. {1:+0.3f}".format(ave_adv, adv))
print("d20 with disadvantage ave: {0},  i.e. {1:+0.3f}".format(ave_dis, dis))


