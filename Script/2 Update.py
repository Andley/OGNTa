# Update all corrections to OGNT

import re

inputFile = "./tmp/OGNT-trimmed.txt"
outputFile = "./OGNTa.txt"


# modifications to morphological code
ChangeList = (
	('018408', 'A-NSF-L'),
	('044656', 'A-NSM'),
	('044681', 'A-NSM'),
	('001339', 'V-I|AAI-3S'),
	('001446', 'N-N|VSF'),
	('001449', 'N-N|VSF'),
	('001456', 'N-N|VSF-L'),
	('002311', 'D-GPN|M'),
	('002313', 'T-GSM|N'),
	('002314', 'A-GSM|N'),
	('002332', 'T-DSN|M'),
	('002729', 'T-GSM|N'),
)


f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()
f.close()

f = open(outputFile,'w',encoding='utf-8')
f.write('\ufeff')
flag = 0

for line in Lines:
	x = re.split("\t", line)
	for OGNTsort, rmac in ChangeList:
		if (x[0] == OGNTsort):
			f.write(x[0]+"\t"+x[1]+"\t"+x[2]+"\t"+x[3]+"\t"+rmac+"\t"+x[5]+"\t"+x[6])
			flag = 1
			break
		else:
			flag = 0
			continue
	if (flag == 0): f.write (line)


f.close()

