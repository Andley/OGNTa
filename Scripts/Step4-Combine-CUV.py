import re

from datetime import date
todays_date = date.today()


inputFile = "./tmp/OGNTa-TC-Ruby.nt"
cuvFile = "./CUV.txt"
outputFile = "./tmp/OGNTa-TC.nt"

f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

f = open(cuvFile,'r',encoding="utf_8_sig")
cuvLines = f.readlines()
f.close()

f = open(outputFile,'w',encoding='utf_8_sig')


for i in range(len(cuvLines)):
	#print(Lines[i])
	Lines[i] = re.sub('<RUBY><ruby><ruby>(.*?)<rt>(.*?)</rt></ruby><rt>(.*?)</rt></ruby><rt>(.*?)</rt></RUBY>', r'\1', Lines[i])
	#print (Lines[i])
	Lines[i] = re.sub('<rt>(.*?)</rt>', r'\1', Lines[i])
	ol = Lines[i].strip()+cuvLines[i]
	f.write(ol)
	#print (ol)

f.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa-TC\nversion.major="+str(todays_date.year)+"\nversion.minor="+str(todays_date.month)+str(todays_date.day)+"\nversion.date="+str(todays_date)+"\ndescription=OGNTa-TC (https://github.com/Andley/OGNTa)")

f.close()
