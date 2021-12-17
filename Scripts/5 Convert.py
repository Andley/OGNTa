import re

from datetime import date
todays_date = date.today()

####### —————————————— Processing OGNTa-RUBY ——————————————

inputFile = "./tmp/OGNTa-marked.txt"
outputFile = "./tmp/OGNTa-Ruby.nt"

# loading data
f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

# processing
f = open(outputFile,'w',encoding='utf_8_sig')
bcv = ""

for ol in Lines:
	if len(ol) > 1:
		x = re.split ("\t", ol)
		# -------------- insert CUV into OGNTa gap verses to meet TheWord Bible requirements.
		if x[0] == "010140": f.write("\n<rt>太17:21</rt> <rt>至於這一類的鬼，若不禱告、禁食，他就不出來（或作：不能趕他出來）。</rt>")
		if x[0] == "010496": f.write("\n<rt>太18:11</rt> <rt>人子來，為要拯救失喪的人。）</rt>")
		if x[0] == "013732": f.write("\n<rt>太23:14</rt> <rt>你們這假冒為善的文士和法利賽人有禍了！因為你們侵吞寡婦的家產，假意做很長的禱告，所以要受更重的刑罰。）</rt>")
		if x[0] == "022759": f.write("\n<rt>可7:16</rt> <rt>有耳可聽的，就應當聽！）</rt>")
		if x[0] == "024509": f.write("\n<rt>可9:44</rt> <rt>你缺了肢體進入永生，強如有兩隻手落到地獄，入那不滅的火裡去。</rt>")
		if x[0] == "024535": f.write("\n<rt>可9:46</rt> <rt>你瘸腿進入永生，強如有兩隻腳被丟在地獄裡。</rt>")
		if x[0] == "025920": f.write("\n<rt>可11:26</rt> <rt>你們若不饒恕人，你們在天上的父也不饒恕你們的過犯。（有古卷無此節）</rt>")
		if x[0] == "028995": f.write("\n<rt>可15:28</rt> <rt>這就應了經上的話說：他被列在罪犯之中。）</rt>")
		if x[0] == "043640": f.write("\n<rt>路17:36</rt> <rt>兩個人在田裡，要取去一個，撇下一個。）</rt>")
		if x[0] == "047735": f.write("\n<rt>路23:17</rt> <rt>每逢這節期，巡撫必須釋放一個囚犯給他們。）</rt>")
		if x[0] == "052024": f.write("\n<rt>約5:4</rt> <rt>因為有天使按時下池子攪動那水，水動之後，誰先下去，無論害甚麼病就痊癒了。）</rt>")
		if x[0] == "070106": f.write("\n<rt>徒8:37</rt> <rt>腓利說：你若是一心相信，就可以。他回答說：我信耶穌基督是神的兒子。）</rt>")
		if x[0] == "074803": f.write("\n<rt>徒15:34</rt> <rt>唯有西拉定意仍住在那裡。）</rt>")
		if x[0] == "077576": f.write("\n<rt>徒19:41</rt> <rt>說了這話，便叫眾人散去。</rt>")
		if x[0] == "080382": f.write("\n<rt>徒24:7</rt> <rt>不料千夫長呂西亞前來，甚是強橫，從我們手中把他奪去，吩咐告他的人到你這裡來。）</rt>")
		if x[0] == "083187": f.write("\n<rt>徒28:29</rt> <rt>保羅說了這話，猶太人議論紛紛的就走了。）</rt>")
		if x[0] == "090276": f.write("\n<rt>羅16:24</rt> <rt>城內管銀庫的以拉都，和兄弟括土問你們安。</rt>")
		if x[0] == "101636": f.write("\n<rt>林後13:14</rt> <rt>願主耶穌基督的恩惠、神的慈愛、聖靈的感動，常與你們眾人同在！</rt>")
		# -------------- insert section break
		# TW3 clipboard monitor does not support </br>, use </br> instead 😂
		if (re.match("¬.*",x[2])): f.write("</br>")
		if (re.match("<strong>¬.*",x[2])): f.write("</br>")
		if (re.match("<em>¬.*",x[2])): f.write("</br>")
		# -------------- align 3Jo 1:15 & Rev 12:18 to meet TheWord Bible requirements.
		if (x[1] == "Rev 12:18") or (x[1] == "3Jo 1:15") or (x[1]== bcv):
			f.write(" ")
		elif (x[1] == "Mat 1:1"):
			bcv = x[1]
			f.write("<rt>"+x[1]+"</rt> ")
		else:
			bcv = x[1]
			f.write("\n")
			f.write("<rt>"+x[1]+"</rt> ")
		# --------------
		x[6] = re.sub("\n","",x[6])
		f.write("<RUBY><ruby><ruby>"+x[2]+"<rt>"+x[6]+"</rt></ruby><rt>"+x[3]+"</rt></ruby><rt>"+x[4]+"</rt></RUBY>")
		# following format does not work for web browser
		#f.write("<ruby>"+x[2]+"<rt>"+x[6]+"</rt><rt>"+x[3]+"</rt><rt>"+x[4]+"</rt></ruby>")
		# ------------- insert paragraph break
		# TW3 clipboard monitor does not support </br>, use </br> instead 😂
		if (re.match(".*¶",x[2])): f.write("</br></br></br>")
		if (re.match(".*¶<strong>",x[2])): f.write("</br></br></br>")
		if (re.match(".*¶<em>",x[2])): f.write("</br></br></br>")

# ---------- 
f.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa-Ruby\nversion.major="+str(todays_date.year)+"\nversion.minor="+str(todays_date.month)+str(todays_date.day)+"\nversion.date="+str(todays_date)+"\ndescription=OGNTa-Ruby (https://github.com/Andley/OGNTa)")

#
f.close()

####### —————————————— Processing OGNTa-TC-RUBY ——————————————

inputFile = "./tmp/OGNTa-TC-marked.txt"
outputFile = "./tmp/OGNTa-TC-Ruby.nt"

# loading data
f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

# processing
f = open(outputFile,'w',encoding='utf_8_sig')
bcv = ""

for ol in Lines:
	if len(ol) > 1:
		x = re.split ("\t", ol)
		# -------------- insert CUV into OGNTa gap verses to meet TheWord Bible requirements.
		if x[0] == "010140": f.write("\n<rt>太17:21</rt> <rt>至於這一類的鬼，若不禱告、禁食，他就不出來（或作：不能趕他出來）。</rt>")
		if x[0] == "010496": f.write("\n<rt>太18:11</rt> <rt>人子來，為要拯救失喪的人。）</rt>")
		if x[0] == "013732": f.write("\n<rt>太23:14</rt> <rt>你們這假冒為善的文士和法利賽人有禍了！因為你們侵吞寡婦的家產，假意做很長的禱告，所以要受更重的刑罰。）</rt>")
		if x[0] == "022759": f.write("\n<rt>可7:16</rt> <rt>有耳可聽的，就應當聽！）</rt>")
		if x[0] == "024509": f.write("\n<rt>可9:44</rt> <rt>你缺了肢體進入永生，強如有兩隻手落到地獄，入那不滅的火裡去。</rt>")
		if x[0] == "024535": f.write("\n<rt>可9:46</rt> <rt>你瘸腿進入永生，強如有兩隻腳被丟在地獄裡。</rt>")
		if x[0] == "025920": f.write("\n<rt>可11:26</rt> <rt>你們若不饒恕人，你們在天上的父也不饒恕你們的過犯。（有古卷無此節）</rt>")
		if x[0] == "028995": f.write("\n<rt>可15:28</rt> <rt>這就應了經上的話說：他被列在罪犯之中。）</rt>")
		if x[0] == "043640": f.write("\n<rt>路17:36</rt> <rt>兩個人在田裡，要取去一個，撇下一個。）</rt>")
		if x[0] == "047735": f.write("\n<rt>路23:17</rt> <rt>每逢這節期，巡撫必須釋放一個囚犯給他們。）</rt>")
		if x[0] == "052024": f.write("\n<rt>約5:4</rt> <rt>因為有天使按時下池子攪動那水，水動之後，誰先下去，無論害甚麼病就痊癒了。）</rt>")
		if x[0] == "070106": f.write("\n<rt>徒8:37</rt> <rt>腓利說：你若是一心相信，就可以。他回答說：我信耶穌基督是神的兒子。）</rt>")
		if x[0] == "074803": f.write("\n<rt>徒15:34</rt> <rt>唯有西拉定意仍住在那裡。）</rt>")
		if x[0] == "077576": f.write("\n<rt>徒19:41</rt> <rt>說了這話，便叫眾人散去。</rt>")
		if x[0] == "080382": f.write("\n<rt>徒24:7</rt> <rt>不料千夫長呂西亞前來，甚是強橫，從我們手中把他奪去，吩咐告他的人到你這裡來。）</rt>")
		if x[0] == "083187": f.write("\n<rt>徒28:29</rt> <rt>保羅說了這話，猶太人議論紛紛的就走了。）</rt>")
		if x[0] == "090276": f.write("\n<rt>羅16:24</rt> <rt>城內管銀庫的以拉都，和兄弟括土問你們安。</rt>")
		if x[0] == "101636": f.write("\n<rt>林後13:14</rt> <rt>願主耶穌基督的恩惠、神的慈愛、聖靈的感動，常與你們眾人同在！</rt>")
		# -------------- insert section break
		# TW3 clipboard monitor does not support </br>, use </br> instead 😂
		if (re.match("¬.*",x[2])): f.write("</br>")
		if (re.match("<strong>¬.*",x[2])): f.write("</br>")
		if (re.match("<em>¬.*",x[2])): f.write("</br>")
		# -------------- align 3Jo 1:15 & Rev 12:18 to meet TheWord Bible requirements.
		if (x[1] == "啟 12:18") or (x[1] == "約三 1:15") or (x[1]== bcv):
			f.write(" ")
		elif (x[1] == "太 1:1"):
			bcv = x[1]
			f.write("<rt>"+x[1]+"</rt> ")
		else:
			bcv = x[1]
			f.write("\n")
			f.write("<rt>"+x[1]+"</rt> ")
		# --------------
		x[6] = re.sub("\n","",x[6])
		f.write("<RUBY><ruby><ruby>"+x[2]+"<rt>"+x[6]+"</rt></ruby><rt>"+x[3]+"</rt></ruby><rt>"+x[4]+"</rt></RUBY>")
		# following format does not work for web browser
		# f.write("<ruby>"+x[2]+"<rt>"+x[6]+"</rt><rt>"+x[3]+"</rt><rt>"+x[4]+"</rt></ruby>")
		# ------------- insert paragraph break
		# TW3 clipboard monitor does not support </br>, use </br> instead 😂
		if (re.match(".*¶",x[2])): f.write("</br></br></br>")
		if (re.match(".*¶<strong>",x[2])): f.write("</br></br></br>")
		if (re.match(".*¶<em>",x[2])): f.write("</br></br></br>")

# ---------- 
f.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa-TC-Ruby\nversion.major="+str(todays_date.year)+"\nversion.minor="+str(todays_date.month)+str(todays_date.day)+"\nversion.date="+str(todays_date)+"\ndescription=OGNTa-TC-Ruby (https://github.com/Andley/OGNTa)")

#
f.close()