# trim original OGNT to mininum data

import re

# ══════ trim interlinear ═══════════════════════

inputFile = "./OpenGNT_version3_3.csv"
outputFile = "./tmp/OGNT-trimmed.txt"

# Trimming OGNT to minimum dataset required for interlinear
# 1-OGNTsort	2-TANTTsort	3-FEATURESsort1-	4-LevinsohnClauseID	5-OTquotation	〔6-BGBsortI｜7-LTsortI｜8-STsortI〕	〔9-Book｜10-Chapter｜11-Verse〕	〔12-OGNTk｜13-OGNTu｜14-OGNTa｜15-lexeme｜16-rmac｜17-sn〕	〔18-BDAGentry｜19-EDNTentry｜20-MounceEntry｜21-GoodrickKohlenbergerNumbers｜22-LN-LouwNidaNumbers〕	〔23-transSBLcap｜24-transSBL｜25-modernGreek｜26-Fonética_Transliteración〕	〔27-TBESG｜28-IT｜29-LT｜30-ST｜31-Español〕	〔32-PMpWord｜33-PMfWord〕	〔34-Note｜35-Mvar｜36-Mlexeme｜37-Mrmac｜38-Msn｜39-MTBESG〕

f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()[1:]
f.close()

f = open(outputFile,'w',encoding="utf_8_sig")
for line in Lines:
	#print (line)
	line = line.replace('\t〔','\t')
	line = line.replace('〕\t','\t')
	line = line.replace('｜','\t')
	x = re.split("\t", line)
	#
	x[27] = x[27].replace(',','')
	x[27] = x[27].replace(';','')
	x[27] = x[27].replace('.','')
	x[27] = x[27].replace(' —','')
	x[27] = x[27].replace(':','')
	#
	x[31] = x[31].replace('<pm>','')
	x[31] = x[31].replace('</pm>',' ')
	x[31] = x[31].replace('[[','⟦')
	x[32] = x[32].replace('<pm>',' ')
	x[32] = x[32].replace('</pm>','')
	x[32] = x[32].replace(']]','⟧')
	#
	x[8] = x[8].replace('40', 'Mat')
	x[8] = x[8].replace('41', 'Mar')
	x[8] = x[8].replace('42', 'Luk')
	x[8] = x[8].replace('43', 'Joh')
	x[8] = x[8].replace('44', 'Act')
	x[8] = x[8].replace('45', 'Rom')
	x[8] = x[8].replace('46', '1Co')
	x[8] = x[8].replace('47', '2Co')
	x[8] = x[8].replace('48', 'Gal')
	x[8] = x[8].replace('49', 'Eph')
	x[8] = x[8].replace('50', 'Php')
	x[8] = x[8].replace('51', 'Col')
	x[8] = x[8].replace('52', '1Th')
	x[8] = x[8].replace('53', '2Th')
	x[8] = x[8].replace('54', '1Ti')
	x[8] = x[8].replace('55', '2Ti')
	x[8] = x[8].replace('56', 'Tit')
	x[8] = x[8].replace('57', 'Phm')
	x[8] = x[8].replace('58', 'Heb')
	x[8] = x[8].replace('59', 'Jas')
	x[8] = x[8].replace('60', '1Pe')
	x[8] = x[8].replace('61', '2Pe')
	x[8] = x[8].replace('62', '1Jo')
	x[8] = x[8].replace('63', '2Jo')
	x[8] = x[8].replace('64', '3Jo')
	x[8] = x[8].replace('65', 'Jud')
	x[8] = x[8].replace('66', 'Rev')
	#
	f.write (x[0]+'\t'+x[8]+' '+x[9]+':'+x[10]+'\t'+x[31]+x[13]+x[32]+'\t'+x[14]+'\t'+x[15]+'\t'+x[26]+'\t'+x[27]+'\n')

f.close()



# ══════ trim Chinese glosses ═══════════════════════


inputFile = "./OpenGNT_interlinear_CUVtc.csv"
outputFile = "./tmp/CUV-Glosses.txt"

f = open(inputFile,'r',encoding="utf-8")
newData = f.read()
f.close()

searchReplace = (
	('｛\d+＃',''),
	('｜\d+｝',''),
	('〈\d+＊','⸂'),
	('｜\d+〉','⸃'),
	('；',''),
	('，',''),
	('。',''),
	('．',''),
	(',',''),
	('〔.*?〕',''),
	('【.*?】',''),
	('\[.*?\]',''),
	('⸃⸂',''),
	('\(bcc.*?\)',''),
	('\(.*?\)',''),
	('\(\*bcc.*?\)',''),
	('\(=bcc.*?\)',''),
	('（\*bcc.*?）',''),
	(' ',''),
	('\*','⸂'),
	('\t⸂','\t'),
	('⸃\n','\n'),
	('\d+\t\n',''),
	('　','')
)

for search, replace in searchReplace:
	newData = re.sub (search, replace, newData)

	
f = open(outputFile,'w',encoding="utf_8_sig")
f.write(newData)
f.close()
