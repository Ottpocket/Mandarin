'''
Randomly generates tables of random numbers.

ARGUMENTS
--------------
nrows: (int) number of rows of numbers. default: 1
ncols: (int) number of columns of numbers. default: 2
digits: (int) number of digits per number. default: 6
time: (int) number of seconds given to memorize pinyin before recall.
      Note: if not given, no second timer will be used
      
EXAMPLES
------------------
1.  Find how long it takes to memorize 2 rows with 5 pinyin characters each
>> python pinyin_generator.py --nrows 2 --ncols 5
2.  Give 1 minute to memorize 10 rows with 3 pinyin characters
>> python pinyin_generator.py --nrows 10 --ncols 3 --time 60
'''
import numpy as np
import argparse
from tqdm import tqdm
from time import sleep, time

parser = argparse.ArgumentParser()
parser.add_argument('--nrows', default=10, type=int)
parser.add_argument('--ncols', default=10, type=int)
parser.add_argument('--digits', default=6, type=int, choices=[i for i in range(9)])
parser.add_argument('--time',  default=-1, type=int)
args = parser.parse_args()
NROWS = args.nrows
NCOLS = args.ncols
DIGITS=args.digits
TIME = args.time


def n_digit_rand(digits = DIGITS):
    digit = ''
    for _ in range(digits):
        digit += str( np.random.choice([i for i in range(10)], size = 1)[0])
    return digit


rand_numbers = [n_digit_rand() for _ in range(NROWS * NCOLS)] 

def print_random_number():
    index = 0
    for row in range(NROWS):
        print(f'{row+1 : 4}: ', end = " ")
        for col in range(NCOLS):
            print(f'{rand_numbers[index] :9}', end='')
            index += 1
        print('')

print_random_number()
if TIME < 0:
    start = time()
    input("Press <Enter> once you have finished")
    print(f'Took {time() - start :.4f} seconds')
else:
    
    for sec in tqdm(range(TIME)):
        sleep(1.)
    print("\033[H\033[J", end="") #from: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-'console'
    input("Press <Enter> key to reveal the pinyin") #https://stackoverflow.com/questions/577467/pause-in-python
    print_random_number()
