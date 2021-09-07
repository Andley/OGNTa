# convert OGNTa into TheWord format

import re

inputFile = "OGNTa.txt"
outputFile = "OGNTa-Ruby.nt"

# loading data
f = open(inputFile,'r',encoding="utf-8")
Lines = f.readlines()
f.close()

# processing
f = open(outputFile,'w',encoding='utf-8')
f.write('\ufeff')
bcv = ""

for ol in Lines:
	if len(ol) > 1:
		x = re.split ("\t", ol)
		# -------------- insert CUV into OGNT gap verses to meet TheWord Bible requirements.
		if x[0] == "010140": f.write("\n<rt>太17:21</rt> <rt>至於這一類的鬼，若不禱告、禁食，他就不出來（或作：不能趕他出來）。</rt>")
		if x[0] == "010496": f.write("\n<rt>太18:11</rt> 〔40｜18｜11〕<rt>人子來，為要拯救失喪的人。）</rt>")
		if x[0] == "013732": f.write("\n<rt>太23:14</rt> 〔40｜23｜14〕<rt>你們這假冒為善的文士和法利賽人有禍了！因為你們侵吞寡婦的家產，假意做很長的禱告，所以要受更重的刑罰。）</rt>")
		if x[0] == "022759": f.write("\n<rt>可7:16</rt> 〔41｜7｜16〕<rt>有耳可聽的，就應當聽！）</rt>")
		if x[0] == "024509": f.write("\n<rt>可9:44</rt> 〔41｜9｜44〕<rt>你缺了肢體進入永生，強如有兩隻手落到地獄，入那不滅的火裡去。</rt>")
		if x[0] == "024535": f.write("\n<rt>可9:46</rt> 〔41｜9｜46〕<rt>你瘸腿進入永生，強如有兩隻腳被丟在地獄裡。</rt>")
		if x[0] == "025920": f.write("\n<rt>可11:26</rt> 〔41｜11｜26〕<rt>你們若不饒恕人，你們在天上的父也不饒恕你們的過犯。（有古卷無此節）</rt>")
		if x[0] == "028995": f.write("\n<rt>可15:28</rt> 〔41｜15｜28〕<rt>這就應了經上的話說：他被列在罪犯之中。）</rt>")
		if x[0] == "043640": f.write("\n<rt>路17:36</rt> 〔42｜17｜36〕<rt>兩個人在田裡，要取去一個，撇下一個。）</rt>")
		if x[0] == "047735": f.write("\n<rt>路23:17</rt> 〔42｜23｜17〕<rt>每逢這節期，巡撫必須釋放一個囚犯給他們。）</rt>")
		if x[0] == "052024": f.write("\n<rt>約5:4</rt> 〔43｜5｜4〕<rt>因為有天使按時下池子攪動那水，水動之後，誰先下去，無論害甚麼病就痊癒了。）</rt>")
		if x[0] == "070106": f.write("\n<rt>徒8:37</rt> 〔44｜8｜37〕<rt>腓利說：你若是一心相信，就可以。他回答說：我信耶穌基督是神的兒子。）</rt>")
		if x[0] == "074803": f.write("\n<rt>徒15:34</rt> 〔44｜15｜34〕<rt>唯有西拉定意仍住在那裡。）</rt>")
		if x[0] == "077576": f.write("\n<rt>徒19:41</rt> 〔44｜19｜41〕<rt>說了這話，便叫眾人散去。</rt>")
		if x[0] == "080382": f.write("\n<rt>徒24:7</rt> 〔44｜24｜7〕<rt>不料千夫長呂西亞前來，甚是強橫，從我們手中把他奪去，吩咐告他的人到你這裡來。）</rt>")
		if x[0] == "083187": f.write("\n<rt>徒28:29</rt> 〔44｜28｜29〕<rt>保羅說了這話，猶太人議論紛紛的就走了。）</rt>")
		if x[0] == "090276": f.write("\n<rt>羅16:24</rt> 〔45｜16｜24〕<rt>城內管銀庫的以拉都，和兄弟括土問你們安。</rt>")
		if x[0] == "101636": f.write("\n<rt>林後13:14</rt> 〔47｜13｜14〕<rt>願主耶穌基督的恩惠、神的慈愛、聖靈的感動，常與你們眾人同在！</rt>")
		# -------------- align 3Jo 1:15 & Rev 12:18 to meet TheWord Bible requirements.
		if (x[1] == "Rev 12:18") or (x[1] == "3Jo 1:15") or (x[1]== bcv):
			f.write(" ")
		elif (x[1] == "Mat 1:1"):
			f.write("<rt>"+x[1]+"</rt> ")
		else:
			bcv = x[1]
			f.write("\n")
			f.write("<rt>"+x[1]+"</rt> ")
		# -------------- insert section break
		if (re.match("¬.*",x[2])): f.write("<hr>")
		# --------------
		ol = re.sub("(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\t(.*?)\n", r" <RUBY><ruby><ruby>\3<rt>\7</rt></ruby><rt>\4</rt></ruby><rt>\5</rt></RUBY>", ol)
		f.write(ol)
		# ------------- insert paragraph break
		if (re.match(".*¶$",x[2])): f.write("<pre></pre>")

# ---------- 
f.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa-Ruby\ndescription=OGNTa (https://github.com/Andley/OGNTa)")

#
f.close()

