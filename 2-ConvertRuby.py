# 

import re

inputFile = "OGNTa.txt"
outputFile = "OGNTa.md"

# loading data
f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()
f.close()

# processing
f = open(outputFile,'w',encoding='utf-8')
bcv = ""
for ol in Lines:
	x = re.split ("\t", ol)
	if x[1] == bcv:
		ol = re.sub("(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\n", r" <RUBY><ruby><ruby>\3<rt>\7</rt></ruby><rt>\4</rt></ruby><rt>\5</rt></RUBY>", ol)
		f.write(ol)
	else:
		ol = re.sub("(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\n", r"\n<rt>\2</rt> <RUBY><ruby><ruby>\3<rt>\7</rt></ruby><rt>\4</rt></ruby><rt>\5</rt></RUBY>", ol)
		bcv = x[1]
		f.write(ol)

#
f.close()