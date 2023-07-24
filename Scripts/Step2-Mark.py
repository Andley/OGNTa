# Mark emphasis on all verbals

import re

####### —————————————— Processing OGNTa ——————————————

inputFile = "./OGNTa.txt"
outputFile1 = "./tmp/OGNTa-marked.txt"

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f1 = open(outputFile1,'w',encoding="utf_8_sig")

for line in Lines:
	x = re.split("\t", line)

	x[2] = re.sub(r"([\.,;·])",r"<strong>\1</strong>",x[2])
	# print (x[2])

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[4])) or (re.match(r'V-...⁞...-\d.',x[4])) or (re.match(r'V-....-\d.',x[4])):
		f1.write(x[0]+"\t"+x[1]+"\t<strong>"+x[2]+"</strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5])

	# add emphasis for participles
	elif (re.match(r'V-..P-...',x[4])) or (re.match(r'V-..P-...⁞...',x[4])) or (re.match(r'V-...P-...',x[4])):
		f1.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5])

	# add emphasis for infinitives
	elif (re.match(r'V-..N',x[4])) or (re.match(r'V-...N',x[4])):
		f1.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5])

	else:
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5])

f1.close()

####### —————————————— Processing OGNTa-TC ——————————————

inputFile = "./OGNTa-TC.txt"
outputFile1 = "./tmp/OGNTa-TC-marked.txt"

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f1 = open(outputFile1,'w',encoding="utf_8_sig")

for line in Lines:
	x = re.split("\t", line)


	x[2] = re.sub(r"([\.,;·])",r"<strong>\1</strong>",x[2])
	# print (x[2])

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[4])) or (re.match(r'V-...⁞...-\d.',x[4])) or (re.match(r'V-....-\d.',x[4])):
		f1.write(x[0]+"\t"+x[1]+"\t<strong>"+x[2]+"</strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5])

	# add emphasis for participles
	elif (re.match(r'V-..P-...',x[4])) or (re.match(r'V-..P-...⁞...',x[4])) or (re.match(r'V-...P-...',x[4])):
		f1.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5])

	# add emphasis for infinitives
	elif (re.match(r'V-..N',x[4])) or (re.match(r'V-...N',x[4])):
		f1.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5])

	else:
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5])

f1.close()
