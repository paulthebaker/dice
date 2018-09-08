# dice

`dice.py` -- library for `Dice` class

## scripts to roll combinations of dice

`roll.py` -- roll NdD (i.e. 4d6)
handles any integer sided die, even nonexistent ones: i.e. 5d3, 1d16

`dice_ave.py` -- compute brute-force average outcome of rolls,
currently non-general

### usage:
roll.py

options:
 * `-l`, `--large=L` : keep only largest `L` dice
 * `-s`, `--small=S` : keep only smallest `S` dice
 * `-r`, `--repeat=M` : repeat roll for `M` trials
 * `-a`, `--average` : compute average of trials

##examples:
character creation - roll 4d6 and keep the largest 3 for each of 6 attributes:
 * `$ python roll.py --repeat=6 --large=3 4d6`

skill check with disadvange - roll 2d20 keep the smallest 1:
 * `$ python roll.py --small=1 2d20`

estimate the average outcome for rolling 5d16 and keeping the best 2:
 * `$ python roll.py --average --repeat=1000 --large=2 5d16`

## TODO:
 * generalize `dice_ave.py`
 * handle combinations of dice (i.e. 1d8 + 1d12)
