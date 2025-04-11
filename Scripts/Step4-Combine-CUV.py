import re

from datetime import date
todays_date = date.today()


inputFile = "../tmp/OGNTa-Ruby.nt"
cuvFile = "../CUV.txt"
outputFile = "../tmp/OGNTa+CUV.nt"

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f = open(cuvFile,'r',encoding="utf_8_sig")
cuvLines = f.readlines()
f.close()
f = open(outputFile,'w',encoding='utf_8_sig')


for i in range(len(cuvLines)):
	Lines[i] = re.sub('<RUBY><ruby><ruby>(.*?)<rt>(.*?)</rt></ruby><rt>(.*?)</rt></ruby><rt>(.*?)</rt></RUBY>', r'\1', Lines[i])
	Lines[i] = re.sub(' +', ' ', Lines[i])
	#print(Lines[i])
	if ("<mark class='paragraph'></mark>" in Lines[i]):
		#print("paragraph")
		Lines[i] = re.sub("<mark class='paragraph'></mark>","",Lines[i])
		ol = Lines[i].strip()+cuvLines[i].strip()+"<mark class='paragraph'></mark>\n"
	else:
		ol = Lines[i].strip()+cuvLines[i]
	f.write(ol)
	#print (ol)

f.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa+CUV\nversion.major="+str(todays_date.year)+"\nversion.minor="+str(todays_date.month)+str(todays_date.day)+"\nversion.date="+str(todays_date)+"\ndescription=OGNTa-Ruby+CUV (https://github.com/Andley/OGNTa)")

f.close()
