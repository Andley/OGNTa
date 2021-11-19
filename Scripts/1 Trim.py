# trim original OGNT to mininum data

import re

inputFile = "./OpenGNT_version3_3.csv"
outputFile = "./tmp/OGNT-trimmed"

# ---------------------------------------------------
f = open(inputFile,'r',encoding="utf-8")
newData = f.read()
f.close()

# Trimming OGNT to minimum dataset required for interlinear
# 1-OGNTsort	2-TANTTsort	3-FEATURESsort1-	4-LevinsohnClauseID	5-OTquotation	〔6-BGBsortI｜7-LTsortI｜8-STsortI〕	〔9-Book｜10-Chapter｜11-Verse〕	〔12-OGNTk｜13-OGNTu｜14-OGNTa｜15-lexeme｜16-rmac｜17-sn〕	〔18-BDAGentry｜19-EDNTentry｜20-MounceEntry｜21-GoodrickKohlenbergerNumbers｜22-LN-LouwNidaNumbers〕	〔23-transSBLcap｜24-transSBL｜25-modernGreek｜26-Fonética_Transliteración〕	〔27-TBESG｜28-IT｜29-LT｜30-ST｜31-Español〕	〔32-PMpWord｜33-PMfWord〕	〔34-Note｜35-Mvar｜36-Mlexeme｜37-Mrmac｜38-Msn｜39-MTBESG〕
newData = re.sub('(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t〔(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\n', r'\1\t\9-\10:\11\t\32\14\33\t\15\t\16\t\27\t\28\n', newData)

# clean-up punctuation marks etc.
newData = re.sub('OGNTsort	Book-Chapter:Verse	PMpWordOGNTaPMfWord	lexeme	rmac	TBESG	IT\n','',newData)
# newData = re.sub ('</pm><pm>',' ', newData)
newData = re.sub ('</pm>',' ', newData)
newData = re.sub ('<pm>',' ', newData)

# Update Book Name Abbreviation
searchReplace = (
	('40-', 'Mat '),
	('41-', 'Mar '),
	('42-', 'Luk '),
	('43-', 'Joh '),
	('44-', 'Act '),
	('45-', 'Rom '),
	('46-', '1Co '),
	('47-', '2Co '),
	('48-', 'Gal '),
	('49-', 'Eph '),
	('50-', 'Php '),
	('51-', 'Col '),
	('52-', '1Th '),
	('53-', '2Th '),
	('54-', '1Ti '),
	('55-', '2Ti '),
	('56-', 'Tit '),
	('57-', 'Phm '),
	('58-', 'Heb '),
	('59-', 'Jas '),
	('60-', '1Pe '),
	('61-', '2Pe '),
	('62-', '1Jo '),
	('63-', '2Jo '),
	('64-', '3Jo '),
	('65-', 'Jud '),
	('66-', 'Rev '),
	('\[\[', '⟦ '),
	('\]\]', '⟧ '),
)

for search, replace in searchReplace:
	newData = re.sub(search, replace, newData)

# generate output file
f = open(outputFile,'w',encoding='utf-8')
# make file encoded "utf-8 with BOM"
f.write('\ufeff')
f.write (newData)
f.close()

