# Mandarin

Command line tool written in python to help the user memorize strings of random pinyin and tones. 

## Example usages

1. Time how fast you can memorise 2 rows of 10 pinyin and tones:
> python pinyin_generator.py --nrows 2 --ncols 10
>>   1:  3-ju     5-wu     3-cuo    5-shang  5-beng   3-kui    5-dao    4-ba     2-ai     1-gen    
>>   2:  4-le     1-bi     3-jing   4-bi     2-shuo   4-shui   4-he     4-pin    5-chao   5-kui 


2. See if you can memorize 10 characters in 1 minute:
> python pinyin_generator.py --nrows 1 --ncols 10 --time 60
>>   1:  1-nang   2-chou   5-jiu    4-ya     4-qin    5-zang   2-ying   1-shuai  4-lan    2-jiao   


## Getting Started

0. To run, you need **python 3.x** with the following packages installed: **numpy** and **tqdm**
1. In command line type the following: *git clone https://github.com/Ottpocket/Mandarin.git*
2. Move to the Mandarin directory in command line. In Linux, this is done via *cd Mandarin*
3. Run the program with *python pinyin_generator.py*

## Arguments 

All arguments are optional.  To add an argument to the program, just call the program with *python pinyin_generator.py --arg1 value --arg2 value*

**nrows**: (int) number of rows of pinyin characters desired. default: 10

**ncols**: (int) number of columns of pinyin characters desired.  default: 10

**time**: (int) number of seconds given to memorize pinyin before recall.  Note: if not given, the program will time how many seconds it takes you to memorise the given pinyin.
