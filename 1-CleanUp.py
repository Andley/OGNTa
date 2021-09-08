
import re

sourceFile = "OpenGNT_version3_3.csv"
abridgedFile = "OGNTa.txt"
outputFile = "OGNTa-Marked.txt"

# ---------------------------------------------------
f = open(sourceFile,'r',encoding="utf-8")
newData = f.read()
f.close()

# Abridging OGNT to minimum dataset required for an interlinear
# 1-OGNTsort	2-TANTTsort	3-FEATURESsort1-	4-LevinsohnClauseID	5-OTquotation	〔6-BGBsortI｜7-LTsortI｜8-STsortI〕	〔9-Book｜10-Chapter｜11-Verse〕	〔12-OGNTk｜13-OGNTu｜14-OGNTa｜15-lexeme｜16-rmac｜17-sn〕	〔18-BDAGentry｜19-EDNTentry｜20-MounceEntry｜21-GoodrickKohlenbergerNumbers｜22-LN-LouwNidaNumbers〕	〔23-transSBLcap｜24-transSBL｜25-modernGreek｜26-Fonética_Transliteración〕	〔27-TBESG｜28-IT｜29-LT｜30-ST｜31-Español〕	〔32-PMpWord｜33-PMfWord〕	〔34-Note｜35-Mvar｜36-Mlexeme｜37-Mrmac｜38-Msn｜39-MTBESG〕
newData = re.sub('(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t〔(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)〕\t〔(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)｜(.*?)〕\n', r'\1\t\9-\10:\11\t\32\14\33\t\15\t\16\t\27\t\28\n', newData)

# clean-up punctuation marks etc.
newData = re.sub('OGNTsort	Book-Chapter:Verse	PMpWordOGNTaPMfWord	lexeme	rmac	TBESG	IT\n','',newData)
newData = re.sub ('</pm><pm>',' ', newData)
newData = re.sub ('</pm>','', newData)
newData = re.sub ('<pm>','', newData)

# generate abridged file
f = open(abridgedFile,'w',encoding='utf-8')
f.write (newData)
f.close()

# ---------------------------------------------------
f = open(abridgedFile,'r',encoding="utf-8")
newData = f.read()
f.close()

# Fine-tuning (Book Name Abbreviation, Verbal emphasis)
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
	(' —','—'),
	('—',' ——'),
	('(.*?\t.*?\t)(.*?)(\t.*?\tV-...-\d.\t)', r'\1**\2**\3'), # V-???-?? add bold emphasis
	('(.*?\t.*?\t)(.*?)(\t.*?\tV-2...-\d.\t)', r'\1**\2**\3'), # V-2???-?? add bold emphasis
	('(.*?\t.*?\t)(.*?)(\t.*?\tV-..P-...\t)', r'\1*\2*\3'), # V-??P-??? add italic emphasis
	('(.*?\t.*?\t)(.*?)(\t.*?\tV-2..P-...\t)', r'\1*\2*\3'), # V-2??P-??? add italic emphasis
	('(.*?\t.*?\t)(.*?)(\t.*?\tV-..N\t)', r'\1*\2*\3'), # V-??N add italic emphasis
	('(.*?\t.*?\t)(.*?)(\t.*?\tV-2..N\t)', r'\1*\2*\3') # V-2??N add italic emphasis
)


for search, replace in searchReplace:
	newData = re.sub(search, replace, newData)

# generate output file
f = open(outputFile,'w',encoding='utf-8')
f.write (newData)
f.close()

