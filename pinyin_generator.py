'''
Randomly generates tables of pinyin with accompanying tones

'''
import numpy as np

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

nrows = 10
ncols = 10
for i in range(nrows):
    print(f'{i+1 : 4}: ', end = " ")
    for i in range(ncols):
        pin_rand = np.random.choice(pinyin, size = 1, replace=True)[0]
        print(f'{pin_rand :8}', end='')
    print('')