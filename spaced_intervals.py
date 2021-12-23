'''
Creates a bank of 2 digit  random numbers.  The numbers are displayed at 1 second 
intervals
ARGUMENTS
--------------
num_chunks: (int) how many chunks to display. default: 15
chunk_size: (int) number of digits per chunk. default: 2
display_time: (float) number of seconds before a new number is displayed. default: 1
max_num: (int) maximum number to be displayed.  default: 99
      
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
parser.add_argument('--num_chunks', default=15, type=int)
parser.add_argument('--chunk_size', default=2, type=int)
parser.add_argument('--display_time', default=1., type=float)
parser.add_argument('--max_num', default=99, type=int)

args = parser.parse_args()
NUM_CHUNKS = args.num_chunks
CHUNK_SIZE = args.chunk_size
DISPLAY_TIME = args.display_time
MAX_NUM = args.max_num

if len(str(MAX_NUM)) >CHUNK_SIZE:
    raise Exception(f'Chunk max number {MAX_NUM} has over {CHUNK_SIZE} digits!')
chunks = [str(num) for num in range(MAX_NUM+1)]
chunks = [num if (len(num) == CHUNK_SIZE) else '0' + num for num in chunks]

def n_digit_rand(digits = chunks):
    digit = np.random.choice(digits, size=1)[0]
    return digit
  
def display_chunks(chunks, sleep_=False):
    for i, chunk in enumerate(chunks):
        if (i % 3 ==0) and (i !=0):
            print('')
        print(f'{chunk}', end=" ", flush=True)
        if sleep_:
            sleep(DISPLAY_TIME)
  
rand_chunks = [n_digit_rand() for _ in range(NUM_CHUNKS)] 

start = time()
display_chunks(chunks=rand_chunks, sleep_=True)

  
input("Press <Enter> once you have finished")
print("\033[H\033[J", end="") #from: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-'console'
print(f'Took {time() - start :.4f} seconds')
input("Press <Enter> to give the numbers")
display_chunks(chunks= rand_chunks, sleep_=False)
