# Mark emphasis on all verbals

import re

####### —————————————— Processing OGNTa ——————————————

inputFile = "./OGNTa.txt"
outputFile = "./tmp/OGNTa-marked.txt"

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f = open(outputFile,'w',encoding="utf_8_sig")


for line in Lines:
	x = re.split("\t", line)

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[4])) or (re.match(r'V-...⁞...-\d.',x[4])) or (re.match(r'V-....-\d.',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<strong>"+x[2]+"</strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])
		#f.write(x[0]+"\t"+x[1]+"\t<strong><font color='#DB4437'>"+x[2]+"</font></strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	# add emphasis for participles
	elif (re.match(r'V-..P-...',x[4])) or (re.match(r'V-..P-...⁞...',x[4])) or (re.match(r'V-...P-...',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])
		#f.write(x[0]+"\t"+x[1]+"\t<b><font color='#4285F4'>"+x[2]+"</font></b>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	# add emphasis for infinitives
	elif (re.match(r'V-..N',x[4])) or (re.match(r'V-...N',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])
		#f.write(x[0]+"\t"+x[1]+"\t<b><font color='#4285F4'>"+x[2]+"</font></b>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	else:
		f.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

f.close()

####### —————————————— Processing OGNTa-TC ——————————————

inputFile = "./OGNTa-TC.txt"
outputFile = "./tmp/OGNTa-TC-marked.txt"

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f = open(outputFile,'w',encoding="utf_8_sig")
# make file encoded "utf-8 with BOM"
#f.write('\ufeff')

for line in Lines:
	x = re.split("\t", line)

	# add emphasis for Verbs
	if (re.match(r'V-...-\d.',x[4])) or (re.match(r'V-...⁞...-\d.',x[4])) or (re.match(r'V-....-\d.',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<strong>"+x[2]+"</strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])
		#can not use <font color='#DB4437'> due to TheWord Bible format constraint ...
		#f.write(x[0]+"\t"+x[1]+"\t<strong><font color='#DB4437'>"+x[2]+"</font></strong>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	# add emphasis for participles
	elif (re.match(r'V-..P-...',x[4])) or (re.match(r'V-..P-...⁞...',x[4])) or (re.match(r'V-...P-...',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])
		#can not use <font color='#DB4437'> due to TheWord Bible format constraint ...
		#f.write(x[0]+"\t"+x[1]+"\t<b><font color='#4285F4'>"+x[2]+"</font></b>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	# add emphasis for infinitives
	elif (re.match(r'V-..N',x[4])) or (re.match(r'V-...N',x[4])):
		f.write(x[0]+"\t"+x[1]+"\t<em>"+x[2]+"</em>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])
		#can not use <font color='#DB4437'> due to TheWord Bible format constraint ...
		#f.write(x[0]+"\t"+x[1]+"\t<b><font color='#4285F4'>"+x[2]+"</font></b>\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

	else:
		f.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+x[4]+"\t"+x[5]+"\t"+x[6])

f.close()