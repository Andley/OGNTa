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

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[7])) or (re.match(r'V-...⁞...-\d.',x[7])) or (re.match(r'V-....-\d.',x[7])):
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t<span class='verb'>"+x[3]+"</span>\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11])

	# add emphasis for participles
	elif (re.match(r'V-..P-...',x[7])) or (re.match(r'V-..P-...⁞...',x[7])) or (re.match(r'V-...P-...',x[7])):
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t<span class='participle'>"+x[3]+"</span>\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11])

	# add emphasis for infinitives
	elif (re.match(r'V-..N',x[7])) or (re.match(r'V-...N',x[7])):
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t<span class='infinitive'>"+x[3]+"</span>\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11])

	else:
		f1.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6]+"\t"+x[7]+"\t"+x[8]+"\t"+x[9]+"\t"+x[10]+"\t"+x[11])

f1.close()