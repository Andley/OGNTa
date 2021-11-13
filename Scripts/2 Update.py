# Update all corrections to OGNT

import re

inputFile = "./tmp/OGNT-trimmed"
outputFile = "./OGNTa.tsv"


# modifications to morphological code
ChangeList = (
('001339', 'V-IAI⁞AAI-3S'),
('001446', 'N-NSF⁞VSF'),
('001449', 'N-NSF⁞VSF'),
('001456', 'N-NSF⁞VSF-L'),
('002311', 'D-GPN⁞GPM'),
('002313', 'T-GSM⁞GSN'),
('002314', 'A-GSM⁞GSN'),
('002332', 'T-DSN⁞DSM'),
('002729', 'T-GSM⁞GSN'),
('018408', 'A-NSF-L'),
('044656', 'A-NSM'),
('044681', 'A-NSM'),
('07490', 'V-IAI⁞AAI-3S'),
('010230', 'V-IAI⁞AAI-3S'),
('011277', 'V-IAI⁞AAI-3S'),
('012521', 'V-IAI⁞AAI-3S'),
('013408', 'V-IAI⁞AAI-3S'),
('014321', 'N-NPM⁞NPF'),
('014722', 'V-PAI⁞PAM-2P'),
('014870', 'V-PAI⁞PAM-2P'),
('015295', 'V-IAI⁞AAI-3S'),
('015338', 'V-IAI⁞AAI-3S'),
('015856', 'A-ASM⁞ASF⁞ASN'),
('016276', 'V-IAI⁞AAI-3S'),
('017996', 'V-IAI⁞AAI-3S'),
('023937', 'V-IAI⁞AAI-3S'),
('024376', 'V-IAI⁞AAI-3S'),
('024873', 'V-IAI⁞AAI-3S'),
('025028', 'V-IAI⁞AAI-3S'),
('026430', 'V-IAI⁞AAI-3S'),
('027324', 'V-PAI⁞PAM-2P'),
('027922', 'V-IAI⁞AAI-3S'),
('030929', 'V-AAI⁞IAI-3S'),
('061790', 'T-GSM⁞GSN'),
('061797', 'T-GSM⁞GSN'),
('111572', 'T-GSM⁞GSN'),
('058604', 'V-PAI⁞PAM-2P'),
('059844', 'V-PAI⁞PAM-2P'),
('059851', 'V-PAI⁞PAM-2P'),
('060735', 'V-PAI⁞PAM-2P'),
('060772', 'V-PAI⁞PAM-2P'),
('040274', 'V-PAI⁞PAM-2P'),
('046258', 'V-PAI⁞PAM-2P'),
('052654', 'V-PAI⁞PAM-2P'),
('081192', 'V-PAI⁞PAM-2P'),
('090732', 'V-PAI⁞PAM-2P'),
('094554', 'V-PAI⁞PAM-2P'),
('102458', 'V-PAI⁞PAM-2P'),
('109852', 'V-PAI⁞PAM-2P'),
('117367', 'V-PAI⁞PAM-2P'),
('120546', 'V-PAI⁞PAM-2P'),
('125856', 'V-PAI⁞PAM-2P'),
('125884', 'V-PAI⁞PAM-2P'),
('126387', 'V-PAI⁞PAM-2P'),
('071398', 'V-IAI⁞AAI-3S'),
('075568', 'V-IAI⁞AAI-3S'),
('079686', 'V-IAI⁞AAI-3S'),
('044497', 'ADV'),
('122411', 'V-PNI⁞PNM-2P'),
('122457', 'V-PNI⁞PNM-2P'),
('122784', 'V-PPI⁞PPM-2P'),
('044085', 'N-ASF⁞ASM'),
('045957', 'N-NPM⁞NPF'),
('049236', 'V-PNP-ASM⁞NSN'),
('050688', 'V-PAS⁞AAS-3S'),
('050951', 'A-GPN⁞GPM'),
('050973', 'A-GPN⁞GPM'),
('053457', 'V-AAS⁞FAI-1S'),
('105014', 'A-GPM⁞GPN'),
('105017', 'A-GPM⁞GPN'),
('105020', 'A-GPM⁞GPN'),
('055128', 'V-PAS⁞AAS-1S'),
('055267', 'T-GPN⁞GPM'),
('055272', 'T-GPN⁞GPM'),
('066321', 'D-DSN⁞DSM'),
('085145', 'A-GSM⁞GSN'),
('085139', 'A-GSM⁞GSN'),
('071563', 'A-GPM⁞GPN'),
('085394', 'A-GSN⁞GSM'),
('085404', 'A-GSN⁞GSM'),
('086768', 'A-APN⁞NPN'),
('125446', 'P-DSM⁞DSN'),
('124694', 'D-DSM⁞DSN'),
('124690', 'R-DSM⁞DSN'),
('124062', 'R-GPN⁞GPF'),
('122410', 'R-DSM⁞DSN'),
('120232', 'A-DPM⁞DPN'),
('120005', 'V-RAI⁞RAM-2P'),
('118918', 'N-NSM⁞NSN'),
('116068', 'A-GSM⁞GSN'),
('108996', 'A-DPN⁞DPM'),
('105687', 'A-GPN⁞GPM'),
('105496', 'V-RAM⁞RAI-2P'),
('103687', 'V-PAS⁞AAS-3S'),
('100496', 'V-PMI⁞PMM-2P'),
('099999', 'D-ASN⁞NSN'),
('095378', 'D-GPN⁞GPF'),
('095354', 'N-ASN⁞NSN'),
('092950', 'A-NSF⁞NSM'),
('091068', 'A-DPN⁞DPM'),
('088635', 'T-DPM⁞DPN'),
('088636', 'A-DPM⁞DPN'),
('088062', 'V-FAI⁞AAS-1S'),
('088057', 'V-FAI⁞AAS-1S'),
('106998', 'V-PEI⁞PEM-2P')
)


f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()
f.close()

f = open(outputFile,'w',encoding='utf-8')
# make file encoded "utf-8 with BOM"
#f.write('\ufeff')
#flag = 0

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

