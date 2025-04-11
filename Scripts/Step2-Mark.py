# Mark emphasis on all verbals

import re

####### —————————————— Processing OGNTa ——————————————

<<<<<<< HEAD
inputFile = "../OGNTa.txt"
outputFile1 = "../tmp/OGNTa-marked.txt"
=======
inputFile = "./OGNTa.txt"
outputFile1 = "./tmp/OGNTa-marked.txt"
>>>>>>> da8c3dc86bf37656ed17846fd1f9e180fcde9a5b

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f1 = open(outputFile1,'w',encoding="utf_8_sig")

for line in Lines:
	x = re.split("\t", line)

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[7])) or (re.match(r'V-...⁞...-\d.',x[7])) or (re.match(r'V-....-\d.',x[7])):
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t<mark class='verb'>"+x[3]+"</mark>\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11]+"\t"+x[12])

	# add emphasis for participles
	elif (re.match(r'V-..P-...',x[7])) or (re.match(r'V-..P-...⁞...',x[7])) or (re.match(r'V-...P-...',x[7])):
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t<mark class='ptc'>"+x[3]+"</mark>\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11]+"\t"+x[12])

	# add emphasis for infinitives
	elif (re.match(r'V-..N',x[7])) or (re.match(r'V-...N',x[7])):
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t<mark class='inf'>"+x[3]+"</mark>\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11]+"\t"+x[12])

	else:
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11]+"\t"+x[12])

f1.close()