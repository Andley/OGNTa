import re

glosses = "./tmp/CUV-Glosses.txt"
inputFile = "./OGNTa.txt"
outputFile = "./OGNTa-TC.txt"

# loading glosses into dictionary
gloss_dict = {}
gloss_file = open(glosses,'r',encoding="utf_8_sig")
for Line in gloss_file:
	# print(Line)
	key, value = Line.split()
	gloss_dict [key] = value

gloss_file.close()

# loading OGNTa

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
newData = f.read()
f.close()

# processing
f = open(outputFile,'w',encoding='utf_8_sig')

for ol in Lines:
	x = re.split ("\t", ol)
	x[6] = gloss_dict.get(x[0], x[5])
	f.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\n")


f.close()


# ---------------------------------------------------
f = open(outputFile,'r',encoding="utf_8_sig")
newData = f.read()
f.close()

# Update Book Name Abbreviation
searchReplace = (
	('Mat ', '太 '),
	('Mar ', '可 '),
	('Luk ', '路 '),
	('Joh ', '約 '),
	('Act ', '徒 '),
	('Rom ', '羅 '),
	('1Co ', '林前 '),
	('2Co ', '林後 '),
	('Gal ', '加 '),
	('Eph ', '弗 '),
	('Php ', '腓 '),
	('Col ', '西 '),
	('1Th ', '帖前 '),
	('2Th ', '帖後 '),
	('1Ti ', '提前 '),
	('2Ti ', '提後 '),
	('Tit ', '多 '),
	('Phm ', '門 '),
	('Heb ', '來 '),
	('Jas ', '雅 '),
	('1Pe ', '彼前 '),
	('2Pe ', '彼後 '),
	('1Jo ', '約一 '),
	('2Jo ', '約二 '),
	('3Jo ', '約三 '),
	('Jud ', '猶 '),
	('Rev ', '啟 ')
)

for search, replace in searchReplace:
	newData = re.sub(search, replace, newData)

f = open(outputFile,'w',encoding='utf_8_sig')
f.write (newData)
f.close()