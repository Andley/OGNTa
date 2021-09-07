
import re

inputFile = "OGNTa.txt"
outputFile = "OGNTa.txt"


# Book Abbreviation
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
	('66-', 'Rev ')
)


# loading data
f = open(inputFile,'r',encoding="utf-8")
newData = f.read()
f.close()

# replace Book number
for search, replace in searchReplace:
    newData = re.sub(search, replace, newData)


f = open(outputFile,'w',encoding='utf-8')
f.write (newData)
f.close()

