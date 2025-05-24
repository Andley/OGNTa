import re

from datetime import date
todays_date = date.today()

####### —————————————— Processing OGNTa-RUBY ——————————————

inputFile = "./tmp/OGNTa-marked.txt"
outputFile1 = "./tmp/OGNTa-Ruby.nt"
outputFile2 = "./tmp/OGNTa-TC-Ruby.nt"
outputFile3 = "./tmp/OGNTa-All-Ruby.nt"

# loading data
f = open(inputFile,'r',encoding="utf_8_sig")
Lines = f.readlines()
f.close()

# processing
f1 = open(outputFile1,'w',encoding='utf_8_sig')
f2 = open(outputFile2,'w',encoding='utf_8_sig')
f3 = open(outputFile3,'w',encoding='utf_8_sig')
bcv = ""

for ol in Lines:
	if len(ol) > 1:
		x = re.split ("\t", ol)
		# -------------- insert CUV into OGNTa gap verses to meet TheWord Bible requirements.
		if x[0] == "010140": 
			f1.write("\n太17:21 至於這一類的鬼，若不禱告、禁食，他就不出來（或作：不能趕他出來）。")
			f2.write("\n太17:21 至於這一類的鬼，若不禱告、禁食，他就不出來（或作：不能趕他出來）。")
			f3.write("\n太17:21 至於這一類的鬼，若不禱告、禁食，他就不出來（或作：不能趕他出來）。")
		if x[0] == "010496": 
			f1.write("\n太18:11 人子來，為要拯救失喪的人。）")
			f2.write("\n太18:11 人子來，為要拯救失喪的人。）")
			f3.write("\n太18:11 人子來，為要拯救失喪的人。）")
		if x[0] == "013732":
			f1.write("\n太23:14 你們這假冒為善的文士和法利賽人有禍了！因為你們侵吞寡婦的家產，假意做很長的禱告，所以要受更重的刑罰。）")
			f2.write("\n太23:14 你們這假冒為善的文士和法利賽人有禍了！因為你們侵吞寡婦的家產，假意做很長的禱告，所以要受更重的刑罰。）")
			f3.write("\n太23:14 你們這假冒為善的文士和法利賽人有禍了！因為你們侵吞寡婦的家產，假意做很長的禱告，所以要受更重的刑罰。）")
		if x[0] == "022759":
			f1.write("\n可7:16 有耳可聽的，就應當聽！）")
			f2.write("\n可7:16 有耳可聽的，就應當聽！）")
			f3.write("\n可7:16 有耳可聽的，就應當聽！）")
		if x[0] == "024509":
			f1.write("\n可9:44 你缺了肢體進入永生，強如有兩隻手落到地獄，入那不滅的火裡去。")
			f2.write("\n可9:44 你缺了肢體進入永生，強如有兩隻手落到地獄，入那不滅的火裡去。")
			f3.write("\n可9:44 你缺了肢體進入永生，強如有兩隻手落到地獄，入那不滅的火裡去。")
		if x[0] == "024535":
			f1.write("\n可9:46 你瘸腿進入永生，強如有兩隻腳被丟在地獄裡。")
			f2.write("\n可9:46 你瘸腿進入永生，強如有兩隻腳被丟在地獄裡。")
			f3.write("\n可9:46 你瘸腿進入永生，強如有兩隻腳被丟在地獄裡。")
		if x[0] == "025920":
			f1.write("\n可11:26 你們若不饒恕人，你們在天上的父也不饒恕你們的過犯。（有古卷無此節）")
			f2.write("\n可11:26 你們若不饒恕人，你們在天上的父也不饒恕你們的過犯。（有古卷無此節）")
			f3.write("\n可11:26 你們若不饒恕人，你們在天上的父也不饒恕你們的過犯。（有古卷無此節）")
		if x[0] == "028995":
			f1.write("\n可15:28 這就應了經上的話說：他被列在罪犯之中。）")
			f2.write("\n可15:28 這就應了經上的話說：他被列在罪犯之中。）")
			f3.write("\n可15:28 這就應了經上的話說：他被列在罪犯之中。）")
		if x[0] == "043640":
			f1.write("\n路17:36 兩個人在田裡，要取去一個，撇下一個。）")
			f2.write("\n路17:36 兩個人在田裡，要取去一個，撇下一個。）")
			f3.write("\n路17:36 兩個人在田裡，要取去一個，撇下一個。）")
		if x[0] == "047735":
			f1.write("\n路23:17 每逢這節期，巡撫必須釋放一個囚犯給他們。）")
			f2.write("\n路23:17 每逢這節期，巡撫必須釋放一個囚犯給他們。）")
			f3.write("\n路23:17 每逢這節期，巡撫必須釋放一個囚犯給他們。）")
		if x[0] == "052024":
			f1.write("\n約5:4 因為有天使按時下池子攪動那水，水動之後，誰先下去，無論害甚麼病就痊癒了。）")
			f2.write("\n約5:4 因為有天使按時下池子攪動那水，水動之後，誰先下去，無論害甚麼病就痊癒了。）")
			f3.write("\n約5:4 因為有天使按時下池子攪動那水，水動之後，誰先下去，無論害甚麼病就痊癒了。）")
		if x[0] == "070106":
			f1.write("\n徒8:37 腓利說：你若是一心相信，就可以。他回答說：我信耶穌基督是神的兒子。）")
			f2.write("\n徒8:37 腓利說：你若是一心相信，就可以。他回答說：我信耶穌基督是神的兒子。）")
			f3.write("\n徒8:37 腓利說：你若是一心相信，就可以。他回答說：我信耶穌基督是神的兒子。）")
		if x[0] == "074803":
			f1.write("\n徒15:34 唯有西拉定意仍住在那裡。）")
			f2.write("\n徒15:34 唯有西拉定意仍住在那裡。）")
			f3.write("\n徒15:34 唯有西拉定意仍住在那裡。）")
		if x[0] == "077576":
			f1.write("\n徒19:41 說了這話，便叫眾人散去。")
			f2.write("\n徒19:41 說了這話，便叫眾人散去。")
			f3.write("\n徒19:41 說了這話，便叫眾人散去。")
		if x[0] == "080382":
			f1.write("\n徒24:7 不料千夫長呂西亞前來，甚是強橫，從我們手中把他奪去，吩咐告他的人到你這裡來。）")
			f2.write("\n徒24:7 不料千夫長呂西亞前來，甚是強橫，從我們手中把他奪去，吩咐告他的人到你這裡來。）")
			f3.write("\n徒24:7 不料千夫長呂西亞前來，甚是強橫，從我們手中把他奪去，吩咐告他的人到你這裡來。）")
		if x[0] == "083187":
			f1.write("\n徒28:29 保羅說了這話，猶太人議論紛紛的就走了。）")
			f2.write("\n徒28:29 保羅說了這話，猶太人議論紛紛的就走了。）")
			f3.write("\n徒28:29 保羅說了這話，猶太人議論紛紛的就走了。）")
		if x[0] == "090276":
			f1.write("\n羅16:24 城內管銀庫的以拉都，和兄弟括土問你們安。")
			f2.write("\n羅16:24 城內管銀庫的以拉都，和兄弟括土問你們安。")
			f3.write("\n羅16:24 城內管銀庫的以拉都，和兄弟括土問你們安。")
		if x[0] == "101636":
			f1.write("\n林後13:14 願主耶穌基督的恩惠、神的慈愛、聖靈的感動，常與你們眾人同在！")
			f2.write("\n林後13:14 願主耶穌基督的恩惠、神的慈愛、聖靈的感動，常與你們眾人同在！")
			f3.write("\n林後13:14 願主耶穌基督的恩惠、神的慈愛、聖靈的感動，常與你們眾人同在！")

		# -------------- align 3Jo 1:15 & Rev 12:18 to meet TheWord Bible requirements.
		if (x[1] == "Rev 12:18") or (x[1] == "3Jo 1:15") or (x[1]== bcv):
			f1.write(" ")
			f2.write(" ")
			f3.write(" ")
		elif (x[1] == "Mat 1:1"):
			bcv = x[1]
			f1.write(x[1]+" ")
			f2.write(x[1]+" ")
			f3.write(x[1]+" ")
		else:
			bcv = x[1]
			f1.write("\n"+x[1]+" ")
			f2.write("\n"+x[1]+" ")
			f3.write("\n"+x[1]+" ")

		# ---------- remove carriage-return at end-of-line
		x[12] = re.sub("\n","",x[12])

		# -------------- poetry
		if (x[2] == "¬"): 
			x[2] = " <mark class='poetry'></mark> "
		# ------------- punctuation marks
		if (re.match("[.,;·—]",x[4])):
			x[4] = " <mark class='punctuation'>"+x[4]+"</mark> "
		# ------------- paragraph
		if (x[5] == "¶"):
			x[5] = " <mark class='paragraph'></mark> "
		

		# ------------- OT quotation
		if (x[10] == "+"):
			f1.write(re.sub("  "," ", x[2]+" <strong><RUBY><ruby><ruby>"+x[3]+"<rt>"+x[8]+"</rt></ruby><rt>"+x[6]+"</rt></ruby><rt>"+x[7]+"</rt></RUBY></strong>"+x[4]+x[5]))
			f2.write(re.sub("  "," ", x[2]+" <strong><RUBY><ruby><ruby>"+x[3]+"<rt>"+x[9]+"</rt></ruby><rt>"+x[6]+"</rt></ruby><rt>"+x[7]+"</rt></RUBY></strong>"+x[4]+x[5]))
			f3.write(re.sub('  ',' ', x[2]+' <strong><RUBY><ruby><ruby>'+x[3]+'<rt>'+x[9]+' '+x[8]+'</rt></ruby><rt>'+x[6]+'∙'+x[12]+'</rt></ruby><rt>'+x[7]+'</rt></RUBY></strong>'+x[4]+x[5]))
		else:
			f1.write(re.sub("  "," ", x[2]+" <RUBY><ruby><ruby>"+x[3]+"<rt>"+x[8]+"</rt></ruby><rt>"+x[6]+"</rt></ruby><rt>"+x[7]+"</rt></RUBY>"+x[4]+x[5]))
			f2.write(re.sub("  "," ", x[2]+" <RUBY><ruby><ruby>"+x[3]+"<rt>"+x[9]+"</rt></ruby><rt>"+x[6]+"</rt></ruby><rt>"+x[7]+"</rt></RUBY>"+x[4]+x[5]))
			f3.write(re.sub('  ','', x[2]+' <RUBY><ruby><ruby>'+x[3]+'<rt>'+x[9]+' '+x[8]+'</rt></ruby><rt>'+x[6]+'∙'+x[12]+'</rt></ruby><rt>'+x[7]+'</rt></RUBY>'+x[4]+x[5]))

# ---------- 
f1.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa-Ruby\nversion.date="+str(todays_date)+"\ndescription=OGNTa-Ruby (https://github.com/Andley/OGNTa)")
f2.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa-TC-Ruby\nversion.date="+str(todays_date)+"\ndescription=OGNTa-TC-Ruby (https://github.com/Andley/OGNTa)")
f3.write("\n\n\nlang=grc\nnotags=1\nshort.title=OGNTa-TC-Ruby\nversion.date="+str(todays_date)+"\ndescription=OGNTa-All-Ruby (https://github.com/Andley/OGNTa)")

f1.close()
f2.close()
f3.close()