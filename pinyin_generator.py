'''
Randomly generates tables of pinyin with accompanying tones
pinyin copy pastaed from https://www.yellowbridge.com/chinese/pinyin-combo.php.

ARGUMENTS
--------------
nrows: (int) number of rows of pinyin characters desired. default: 10
ncols: (int) number of columns of pinyin characters desired.  default: 10
time: (int) number of seconds given to memorize pinyin. 
      Note: if not given, no second timer will be used
      
EXAMPLES
------------------
1.  Give 2 rows with 5 pinyin characters each
>> python pinyin_generator.py --nrows 2 --ncols 5

2.  Give 10 rows with 3 pinyin characters each and a 1 minute timer.
>> python pinyin_generator.py --nrows 10 --ncols 3 --time 60

'''
import numpy as np
import argparse
from tqdm import tqdm
from time import sleep, time

parser = argparse.ArgumentParser()
parser.add_argument('--nrows', default=10, type=int)
parser.add_argument('--ncols', default=10, type=int)
parser.add_argument('--time',  default=-1, type=int)
args = parser.parse_args()
NROWS = args.nrows
NCOLS = args.ncols
TIME = args.time
pinyin = '''
	a	ba	pa	ma	fa	da	ta	na	la	ga	ka	ha				zha	cha	sha		za	ca	sa	
	o	bo	po	mo	fo																	
	e			me		de	te	ne	le	ge	ke	he				zhe	che	she	re	ze	ce	se	
	ai	bai	pai	mai		dai	tai	nai	lai	gai	kai	hai				zhai	chai	shai		zai	cai	sai	
	ei	bei	pei	mei	fei	dei	tei	nei	ei	gei	kei	hei				zhei		shei		zei			
	ao	bao	pao	mao		dao	tao	nao	lao	gao	kao	hao				zhao	chao	shao	rao	zao	cao	sao	
	ou		pou	mou	fou	dou	tou	nou	lou	gou	kou	hou				zhou	chou	shou	rou	zou	cou	sou	
	an	ban	pan	man	fan	dan	tan	nan	lan	gan	kan	han				zhan	chan	shan	ran	zan	can	san	
	ang	bang	pang	mang	fang	dang	tang	nang	lang	gang	kang	hang				zhang	chang	shang	rang	zang	cang	sang	
	en	ben	pen	men	fen	den		nen		gen	ken	hen				zhen	chen	shen	ren	zen	cen	sen	
	eng	beng	peng	meng	feng	deng	teng	neng	leng	geng	keng	heng				zheng	cheng	sheng	reng	zeng	ceng	seng	
	er																						
	wu	bu	pu	mu	fu	du	tu	nu	lu	gu	ku	hu				zhu	chu	shu	ru	zu	cu	su	
	wa									gua	kua	hua				zhua	chua	shua	rua				
	wo					duo	tuo	nuo	luo	guo	kuo	huo				zhuo	chuo	shuo	ruo	zuo	cuo	suo	
	wai									guai	kuai	huai				zhuai	chuai	shuai					
	wei					dui	tui			gui	kui	hui				zhui	chui	shui	rui	zui	cui	sui	
	wan					duan	tuan	nuan	luan	guan	kuan	huan				zhuan	chuan	shuan	ruan	zuan	cuan	suan	
	wang									guang	kuang	huang				zhuang	chuang	shuang					
	wen					dun	tun	nun	lun	gun	kun	hun				zhun	chun	shun	run	zun	cun	sun	
	weng																						
						dong	tong	nong	long	gong	kong	hong				zhong	chong		rong	zong	cong	song	
			zhi	chi	shi	ri	zi	ci	si	
	yi	bi	pi	mi		di	ti	ni	li				ji	qi	xi								
	ya					dia			lia				jia	qia	xia	
	ye	bie	pie	mie		die	tie	nie	lie				jie	qie	xie	
	yao	biao	piao	miao		diao	tiao	niao	liao				jiao	qiao	xiao	
	you			miu		diu		niu	liu				jiu	qiu	xiu	
	yan	bian	pian	mian		dian	tian	nian	lian				jian	qian	xian	
	yang							niang	liang				jiang	qiang	xiang	
	yin	bin	pin	min				nin	lin				jin	qin	xin	
	ying	bing	ping	ming		ding	ting	ning	ling				jing	qing	xing	
yu							nü	lü				ju	qu	xu	
	yue							nüe	lüe				jue	que	xue	
	yuan												juan	quan	xuan	
	yun												jun	qun	xun	
	yong												jiong	qiong	xiong '''

pinyin = [name if '\n' not in name else name.replace('\n','') for name in pinyin.split('\t') if name not in ['\n', '']]

pin_rand = np.random.choice(pinyin, size = NROWS * NCOLS, replace=True)
tone =  np.random.choice([1,2,3,4,5], size = NROWS * NCOLS, replace = True)
words = [f'{tone[i]}-{pin_rand[i]}' for i in range(NROWS * NCOLS)]

def print_random_pinyin():
    index = 0
    for row in range(NROWS):
        print(f'{row+1 : 4}: ', end = " ")
        for col in range(NCOLS):
            print(f'{words[index] :9}', end='')
            index += 1
        print('')

print_random_pinyin()
if TIME < 0:
    start = time()
    input("Press <Enter> once you have finished")
    print(f'Took {time() - start :.4f} seconds')
else:
    
    for sec in tqdm(range(TIME)):
        sleep(1.)
    print("\033[H\033[J", end="") #from: https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-'console'
    input("Press <Enter> key to reveal the pinyin") #https://stackoverflow.com/questions/577467/pause-in-python
    print_random_pinyin()
