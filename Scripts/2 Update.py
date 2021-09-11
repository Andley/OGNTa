# Update all corrections to OGNT

import re

inputFile = "./tmp/OGNT-trimmed.txt"
outputFile = "./OGNTa.txt"


# modifications to morphological code
ChangeList = (
	('001339', 'V-I|AAI-3S'),
	('001446', 'N-N|VSF'),
	('001449', 'N-N|VSF'),
	('001456', 'N-N|VSF-L'),
	('002311', 'D-GPN|M'),
	('002313', 'T-GSM|N'),
	('002314', 'A-GSM|N'),
	('002332', 'T-DSN|M'),
	('002729', 'T-GSM|N'),
	('018408', 'A-NSF-L'),
	('044656', 'A-NSM'),
	('044681', 'A-NSM'),
	('07490', 'V-I|AAI-3S'),
	('010230', 'V-I|AAI-3S'),
	('011277', 'V-I|AAI-3S'),
	('012521', 'V-I|AAI-3S'),
	('013408', 'V-I|AAI-3S'),
	('014321', 'N-NPM|F'),
	('014722', 'V-PAI|M-2P'),
	('014870', 'V-PAI|M-2P'),
	('015295', 'V-I|AAI-3S'),
	('015338', 'V-I|AAI-3S'),
	('015856', 'A-ASM|F|N'),
	('016276', 'V-I|AAI-3S'),
	('017996', 'V-I|AAI-3S'),
	('023937', 'V-I|AAI-3S'),
	('024376', 'V-I|AAI-3S'),
	('024873', 'V-I|AAI-3S'),
	('025028', 'V-I|AAI-3S'),
	('026430', 'V-I|AAI-3S'),
	('027324', 'V-PAI|M-2P'),
	('027922', 'V-I|AAI-3S'),
	('030929', 'V-A|IAI-3S'),
	('061790', 'T-GSM|N'),
	('061797', 'T-GSM|N'),
	('111572', 'T-GSM|N'),
	('058604', 'V-PAI|M-2P'),
	('059844', 'V-PAI|M-2P'),
	('059851', 'V-PAI|M-2P'),
	('060735', 'V-PAI|M-2P'),
	('060772', 'V-PAI|M-2P'),
	('040274', 'V-PAI|M-2P'),
	('046258', 'V-PAI|M-2P'),
	('052654', 'V-PAI|M-2P'),
	('081192', 'V-PAI|M-2P'),
	('090732', 'V-PAI|M-2P'),
	('094554', 'V-PAI|M-2P'),
	('102458', 'V-PAI|M-2P'),
	('109852', 'V-PAI|M-2P'),
	('117367', 'V-PAI|M-2P'),
	('120546', 'V-PAI|M-2P'),
	('125856', 'V-PAI|M-2P'),
	('125884', 'V-PAI|M-2P'),
	('126387', 'V-PAI|M-2P'),
	('071398', 'V-I|AAI-3S'),
	('075568', 'V-I|AAI-3S'),
	('079686', 'V-I|AAI-3S'),
	('044497', 'ADV'),
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

