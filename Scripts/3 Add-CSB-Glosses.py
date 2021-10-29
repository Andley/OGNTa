import re

glosses = "./CSB-Glosses"
inputFile = "./OGNTa.tsv"
outputFile = "./OGNTa-TC.tsv"

# loading glosses into dictionary
gloss_dict = {}
gloss_file = open(glosses,'r',encoding="utf-8")
for Line in gloss_file:
	key, value = Line.split()
	gloss_dict [key] = value

gloss_file.close()

# loading OGNTa

f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()
f.close()

# processing
f = open(outputFile,'w',encoding='utf-8')
# make file encoded "utf-8 with BOM"
#f.write('\ufeff')

for ol in Lines:
	x = re.split ("\t", ol)
	x[6] = gloss_dict.get(x[0], x[5])
	f.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\n")


f.close()