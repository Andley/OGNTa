# Mark emphasis on all verbals

import re

####### —————————————— Processing OGNTa ——————————————

inputFile = "./OGNTa.tsv"
outputFile = "./tmp/OGNTa-marked"

f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()
f.close()

f = open(outputFile,'w',encoding="utf-8")
# make file encoded "utf-8 with BOM"
f.write('\ufeff')

for line in Lines:
	x = re.split("\t", line)

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[4])) or (re.match(r'V-....-\d.',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<strong>"+x[2]+"</strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	# add emphasis for participles & infinitives
	elif (re.match(r'V-..P-...',x[4])) or (re.match(r'V-...P-...',x[4])) or (re.match(r'V-..N',x[4])) or (re.match(r'V-...N',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	else:
		f.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

f.close()

####### —————————————— Processing OGNTa-TC ——————————————

inputFile = "./OGNTa-TC.tsv"
outputFile = "./tmp/OGNTa-TC-marked"

f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()
f.close()

f = open(outputFile,'w',encoding="utf-8")
# make file encoded "utf-8 with BOM"
f.write('\ufeff')

for line in Lines:
	x = re.split("\t", line)

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[4])) or (re.match(r'V-....-\d.',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<strong>"+x[2]+"</strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	# add emphasis for participles & infinitives
	elif (re.match(r'V-..P-...',x[4])) or (re.match(r'V-...P-...',x[4])) or (re.match(r'V-..N',x[4])) or (re.match(r'V-...N',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	else:
		f.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

f.close()