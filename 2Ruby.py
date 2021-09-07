# 

import re
import code

#

inputFile = 'sample.txt'
outputFile = 'OGNTa.ruby'

# loading data
f = open(inputFile,'r',encoding="utf-8")
newData = f.read()
f.close()

# processing
newData = re.sub("(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\n", r"<rt>\2 \3:\4</rt> <RUBY><ruby><ruby>\10 \5 \11<rt>\8</rt></ruby><rt>\6</rt></ruby><rt>\7</rt></RUBY>", newData)
print (newData)

# save file
f = open(outputFile,'w',encoding='utf-8')
f.write(newData)
f.close()