# OGNTa (OpenGNT Abridged)

## 1) Description

This is an abridged and updated version of [OpenGNTOGNT 3.3](https://github.com/eliranwong/OpenGNT). There are two main files:

**OGNTa.txt** = the main file of OGNTa Project, abridged and updated from OpenGNT_version3_3.csv ([BASE TEXT](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip))

**OGNTa-TC.txt** = OGNTa.txt with Traditional Chinese glosses adapted from [OpenGNT_interlinear_CUVtc.csv](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_interlinear_CUVtc.csv.zip)

## 2) Structure Changes

abridged to the following tab-separated columns:
-  OGNTsort = sort numbers of all words of the base text of OGNT.
-  reference = scripture reference in Book-Chapter:Verse format.
-  Greek = Greek text, comprised of PMpWord/OGNTa/PMfWord, where:
   - PMpWord = punctuation mark(s) preceding the main word.
     - `[[` changed to `⟦`
     - `]]` changed to `⟧`
   - OGNTa = Greek word of OGNT in accented form.
   - PMfWord = punctuation mark(s) following the main word.
-  lemma = Greek word of OGNT in lexical form.
-  rmac = Robinson's Morphological Analysis Codes.
-  IT = context-sensitive English glossess (from Berean Interlinear Bible)
-  TC = context-sensitive Chinese glossess, within which:
  - `⸂`/`⸃` mark the beginning/ending of additional CUV text that are not aligned to the lemma

For example :
| OGNTsort | reference | Greek       | lemma   | rmac    | IT/TC         |
| -------- | --------- | ----------- | ------- | ------- | ------------- |
| 000001   | Mat 1:1   | Βίβλος      | βίβλος  | N-NSF   | [The] book    |
| 000172   | 太 1:11   | Βαβυλῶνος.¶ | Βαβυλών | N-GSF-L | 巴比倫⸂的時候 |
| 000382   | Mat 1:23  | ¬Ἰδοὺ       | ἰδού    | INJ     | look!         |
| 029617   | Mar 16:20 | ⟦ πάντα     | πᾶς     | A-APN   | all           |


## 3) Content Changes

### 3.1) text corrections


### 3.2) punctuation modifications

| OGNTsort | reference | OpenGNT_version3_3 | OGNTa       |
| -------- | --------- | ------------------ | ----------- |
| 122411   | 1Pe 1:6   | ἀγαλλιᾶσθε         | ἀγαλλιᾶσθε, |

### 3.3) lemma corrections

| OGNTsort | reference | OpenGNT_version3_3 | OGNTa |
| -------- | --------- | ------------------ | ----- |
| 009596   | Mat 16:21 | δέω                | δεῖ   |
| 009956   | Mat 17:10 | δέω                | δεῖ   |
| 014302   | Mat 24:6  | δέω                | δεῖ   |
| 016649   | Mat 26:54 | δέω                | δεῖ   |
| 023566   | Mar 8:31  | δέω                | δεῖ   |
| 023932   | Mar 9:11  | δέω                | δεῖ   |
| 026948   | Mar 13:7  | δέω                | δεῖ   |
| 027001   | Mar 13:10 | δέω                | δεῖ   |
| 031636   | Luk 2:49  | δέω                | δεῖ   |
| 033025   | Luk 4:43  | δέω                | δεῖ   |
| 037074   | Luk 9:22  | δέω                | δεῖ   |
| 039844   | Luk 12:12 | δέω                | δεῖ   |
| 040904   | Luk 13:14 | δέω                | δεῖ   |
| 041255   | Luk 13:33 | δέω                | δεῖ   |
| 043475   | Luk 17:25 | δέω                | δεῖ   |
| 044413   | Luk 19:5  | δέω                | δεῖ   |
| 045930   | Luk 21:9  | δέω                | δεῖ   |
| 046934   | Luk 22:37 | δέω                | δεῖ   |
| 048405   | Luk 24:7  | δέω                | δεῖ   |
| 049000   | Luk 24:44 | δέω                | δεῖ   |
| 050523   | Joh 3:7   | δέω                | δεῖ   |
| 050638   | Joh 3:14  | δέω                | δεῖ   |
| 050942   | Joh 3:30  | δέω                | δεῖ   |
| 051472   | Joh 4:24  | δέω                | δεῖ   |
| 055995   | Joh 9:4   | δέω                | δεῖ   |
| 056915   | Joh 10:16 | δέω                | δεῖ   |
| 058868   | Joh 12:34 | δέω                | δεῖ   |
| 063762   | Joh 20:9  | δέω                | δεῖ   |
| 065173   | Act 1:21  | δέω                | δεῖ   |
| 066483   | Act 3:21  | δέω                | δεῖ   |
| 066824   | Act 4:12  | δέω                | δεῖ   |
| 067831   | Act 5:29  | δέω                | δεῖ   |
| 070264   | Act 9:6   | δέω                | δεῖ   |
| 070437   | Act 9:16  | δέω                | δεῖ   |
| 074136   | Act 14:22 | δέω                | δεῖ   |
| 074335   | Act 15:5  | δέω                | δεῖ   |
| 075462   | Act 16:30 | δέω                | δεῖ   |
| 077212   | Act 19:21 | δέω                | δεῖ   |
| 078187   | Act 20:35 | δέω                | δεῖ   |
| 079844   | Act 23:11 | δέω                | δεῖ   |
| 080911   | Act 25:10 | δέω                | δεῖ   |
| 082267   | Act 27:24 | δέω                | δεῖ   |
| 082299   | Act 27:26 | δέω                | δεῖ   |
| 086734   | Rom 8:26  | δέω                | δεῖ   |
| 088475   | Rom 12:3  | δέω                | δεῖ   |
| 093069   | 1Co 8:2   | δέω                | δεῖ   |
| 094447   | 1Co 11:19 | δέω                | δεῖ   |
| 096329   | 1Co 15:25 | δέω                | δεῖ   |
| 096736   | 1Co 15:53 | δέω                | δεῖ   |
| 098679   | 2Co 5:10  | δέω                | δεῖ   |
| 106219   | Eph 6:20  | δέω                | δεῖ   |
| 109265   | Col 4:4   | δέω                | δεῖ   |
| 109287   | Col 4:6   | δέω                | δεῖ   |
| 110368   | 1Th 4:1   | δέω                | δεῖ   |
| 111636   | 2Th 3:7   | δέω                | δεῖ   |
| 112305   | 1Ti 3:2   | δέω                | δεῖ   |
| 112362   | 1Ti 3:7   | δέω                | δεῖ   |
| 112461   | 1Ti 3:15  | δέω                | δεῖ   |
| 113772   | 2Ti 2:6   | δέω                | δεῖ   |
| 114032   | 2Ti 2:24  | δέω                | δεῖ   |
| 114732   | Tit 1:7   | δέω                | δεῖ   |
| 114793   | Tit 1:11  | δέω                | δεῖ   |
| 114802   | Tit 1:11  | δέω                | δεῖ   |
| 115884   | Heb 2:1   | δέω                | δεῖ   |
| 119181   | Heb 11:6  | δέω                | δεῖ   |
| 124957   | 2Pe 3:11  | δέω                | δεῖ   |
| 128176   | Rev 1:1   | δέω                | δεῖ   |
| 129808   | Rev 4:1   | δέω                | δεῖ   |
| 132320   | Rev 10:11 | δέω                | δεῖ   |
| 132436   | Rev 11:5  | δέω                | δεῖ   |
| 135212   | Rev 17:10 | δέω                | δεῖ   |
| 136607   | Rev 20:3  | δέω                | δεῖ   |
| 137703   | Rev 22:6  | δέω                | δεῖ   |


### 3.4) rmac corrections

| OGNTsort | reference | OpenGNT_version3_3 | OGNTa    |
| -------- | --------- | ------------------ | -------- |
| 000891   | Mat 2:23  | ADV                | CONJ     |
| 014871   | Mat 24:43 | ADV                | CONJ     |
| 016647   | Mat 26:54 | ADV                | CONJ     |
| 018408   | Mar 1:5   | N-NSF-L            | A-NSF-L  |
| 019328   | Mar 2:16  | ADV                | CONJ     |
| 023926   | Mar 9:11  | ADV                | CONJ     |
| 024224   | Mar 9:28  | ADV                | CONJ     |
| 025128   | Mar 10:33 | ADV                | CONJ     |
| 030349   | Luk 1:43  | ADV                | CONJ     |
| 033721   | Luk 5:36  | ADV                | CONJ     |
| 038041   | Luk 10:11 | ADV                | CONJ     |
| 038188   | Luk 10:20 | ADV                | CONJ     |
| 040275   | Luk 12:39 | ADV                | CONJ     |
| 044497   | Luk 19:11 | PREP               | ADV      |
| 044656   | Luk 19:21 | P-NSM              | A-NSM    |
| 044681   | Luk 19:22 | P-NSM              | A-NSM    |
| 047331   | Luk 22:61 | ADV                | CONJ     |
| 048999   | Luk 24:44 | ADV                | CONJ     |
| 051666   | Joh 4:37  | ADV                | CONJ     |
| 053269   | Joh 6:29  | ADV                | CONJ     |
| 053447   | Joh 6:39  | ADV                | CONJ     |
| 053471   | Joh 6:40  | ADV                | CONJ     |
| 056390   | Joh 9:25  | ADV                | CONJ     |
| 056465   | Joh 9:30  | ADV                | CONJ     |
| 058273   | Joh 11:57 | ADV                | CONJ     |
| 059756   | Joh 13:34 | ADV                | CONJ     |
| 059762   | Joh 13:34 | ADV                | CONJ     |
| 060562   | Joh 15:8  | ADV                | CONJ     |
| 060630   | Joh 15:12 | ADV                | CONJ     |
| 060727   | Joh 15:17 | ADV                | CONJ     |
| 060880   | Joh 15:25 | ADV                | CONJ     |
| 061545   | Joh 17:3  | ADV                | CONJ     |
| 061569   | Joh 17:4  | ADV                | CONJ     |
| 062139   | Joh 18:9  | ADV                | CONJ     |
| 062758   | Joh 18:39 | ADV                | CONJ     |
| 063761   | Joh 20:9  | ADV                | CONJ     |
| 064700   | Joh 21:23 | ADV                | CONJ     |
| 075553   | Act 16:36 | ADV                | CONJ     |
| 075931   | Act 17:15 | ADV                | CONJ     |
| 078184   | Act 20:35 | ADV                | CONJ     |
| 078198   | Act 20:35 | ADV                | CONJ     |
| 078239   | Act 20:38 | ADV                | CONJ     |
| 078863   | Act 21:31 | ADV                | CONJ     |
| 080479   | Act 24:14 | ADV                | CONJ     |
| 080573   | Act 24:19 | V-2PAN             | V-PAN    |
| 080603   | Act 24:21 | ADV                | CONJ     |
| 083101   | Act 28:25 | ADV                | CONJ     |
| 083744   | Rom 1:32  | ADV                | CONJ     |
| 083812   | Rom 2:3   | ADV                | CONJ     |
| 085551   | Rom 6:6   | ADV                | CONJ     |
| 086230   | Rom 7:21  | ADV                | CONJ     |
| 086976   | Rom 9:2   | ADV                | CONJ     |
| 087050   | Rom 9:6   | ADV                | CONJ     |
| 087551   | Rom 10:5  | ADV                | CONJ     |
| 088251   | Rom 11:25 | ADV                | CONJ     |
| 088917   | Rom 13:11 | ADV                | CONJ     |
| 089866   | Rom 15:31 | ADV                | CONJ     |
| 090521   | 1Co 1:12  | ADV                | CONJ     |
| 090738   | 1Co 1:26  | ADV                | CONJ     |
| 092764   | 1Co 7:26  | ADV                | CONJ     |
| 094529   | 1Co 11:23 | ADV                | CONJ     |
| 096028   | 1Co 15:3  | ADV                | CONJ     |
| 096039   | 1Co 15:4  | ADV                | CONJ     |
| 096042   | 1Co 15:4  | ADV                | CONJ     |
| 096052   | 1Co 15:5  | ADV                | CONJ     |
| 096692   | 1Co 15:50 | ADV                | CONJ     |
| 098757   | 2Co 5:14  | ADV                | CONJ     |
| 099629   | 2Co 8:9   | ADV                | CONJ     |
| 099918   | 2Co 9:2   | ADV                | CONJ     |
| 100292   | 2Co 10:7  | ADV                | CONJ     |
| 100354   | 2Co 10:11 | ADV                | CONJ     |
| 100649   | 2Co 11:10 | ADV                | CONJ     |
| 101833   | Gal 1:13  | ADV                | CONJ     |
| 103082   | Gal 4:18  | V-2PAN             | V-PAN    |
| 103099   | Gal 4:20  | V-2PAN             | V-PAN    |
| 105498   | Eph 5:5   | ADV                | CONJ     |
| 106359   | Php 1:6   | ADV                | CONJ     |
| 106424   | Php 1:9   | ADV                | CONJ     |
| 106596   | Php 1:20  | ADV                | CONJ     |
| 106726   | Php 1:27  | ADV                | CONJ     |
| 107012   | Php 2:16  | ADV                | CONJ     |
| 107088   | Php 2:22  | ADV                | CONJ     |
| 107119   | Php 2:25  | A-NSN              | A-ASN    |
| 109400   | Col 4:12  | ADV                | CONJ     |
| 110591   | 1Th 4:15  | ADV                | CONJ     |
| 111689   | 2Th 3:10  | ADV                | CONJ     |
| 111912   | 1Ti 1:9   | ADV                | CONJ     |
| 112009   | 1Ti 1:15  | ADV                | CONJ     |
| 112077   | 1Ti 1:18  | ADV                | CONJ     |
| 113652   | 2Ti 1:15  | ADV                | CONJ     |
| 114072   | 2Ti 3:1   | ADV                | CONJ     |
| 122152   | Jas 5:11  | ADV                | CONJ     |
| 124363   | 2Pe 1:20  | ADV                | CONJ     |
| 124797   | 2Pe 3:3   | ADV                | CONJ     |
| 124838   | 2Pe 3:5   | ADV                | CONJ     |
| 124891   | 2Pe 3:8   | ADV                | CONJ     |
| 125200   | 1Jo 1:5   | ADV                | CONJ     |
| 126106   | 1Jo 3:11  | ADV                | CONJ     |
| 126321   | 1Jo 3:23  | ADV                | CONJ     |
| 126568   | 1Jo 4:10  | ADV                | CONJ     |
| 126574   | 1Jo 4:10  | ADV                | CONJ     |
| 126803   | 1Jo 4:21  | ADV                | CONJ     |
| 126862   | 1Jo 5:3   | ADV                | CONJ     |
| 127033   | 1Jo 5:11  | ADV                | CONJ     |
| 127094   | 1Jo 5:14  | ADV                | CONJ     |
| 127342   | 2Jo 1:6   | ADV                | CONJ     |
| 127356   | 2Jo 1:6   | ADV                | CONJ     |
| 127530   | 3Jo 1:4   | ADV                | CONJ     |
| 128743   | Rev 2:6   | ADV                | CONJ     |
| 129083   | Rev 2:20  | V-2PAI-2S          | V-PAI-2S |
| 129279   | Rev 3:1   | ADV                | CONJ     |
| 129282   | Rev 3:1   | ADV                | CONJ     |
| 129619   | Rev 3:15  | ADV                | CONJ     |

### 3.5) rmac Verbal system revamped 
- Secondary Tense-Forms code simplified to single letter lower-case letter.
  - Second Aorist: 2A → A
  - Second Future: 2F → F
  - Second Perfect: 2R → R
  - Second Pluperfect: 2L → L
- Voice code simplified to relect current trend in scholarship ---- not implemented yet, to-be-decided
  - Passive: P → 
  - Middle: M → 
  - Either middle or passive: E → 
  - Middle Deponent: D → 
  - Middle or passive Deponent: N → 
  - Passive Deponent: O → 


### 3.6) rmac enhancements

| OGNTsort | reference | OpenGNT_version3_3 | OGNTa         |
| -------- | --------- | ------------------ | ------------- |
| 001339   | Mat 4:7   | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 001446   | Mat 4:15  | N-NSF              | N-NSF⁞VSF     |
| 001449   | Mat 4:15  | N-NSF              | N-NSF⁞VSF     |
| 001456   | Mat 4:15  | N-NSF-L            | N-NSF⁞VSF-L   |
| 002311   | Mat 5:37  | D-GPN              | D-GPN⁞GPM     |
| 002313   | Mat 5:37  | T-GSM              | T-GSM⁞GSN     |
| 002314   | Mat 5:37  | A-GSM              | A-GSM⁞GSN     |
| 002332   | Mat 5:39  | T-DSN              | T-DSN⁞DSM     |
| 002729   | Mat 6:13  | T-GSN              | T-GSM⁞GSN     |
| 010230   | Mat 17:26 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 011277   | Mat 19:21 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 012521   | Mat 21:27 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 013408   | Mat 22:37 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 014321   | Mat 24:7  | N-NPM              | N-NPM⁞NPF     |
| 014722   | Mat 24:33 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 014870   | Mat 24:43 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 015295   | Mat 25:21 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 015338   | Mat 25:23 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 015856   | Mat 26:7  | N-ASN              | A-ASM⁞ASF⁞ASN |
| 016276   | Mat 26:34 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 017996   | Mat 27:65 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 023937   | Mar 9:12  | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 024376   | Mar 9:38  | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 024873   | Mar 10:20 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 025028   | Mar 10:29 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 026430   | Mar 12:24 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 027324   | Mar 13:29 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 027922   | Mar 14:29 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 030929   | Luk 2:7   | V-AAI-3S           | V-AAI⁞IAI-3S  |
| 040274   | Luk 12:39 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 044085   | Luk 18:25 | N-ASF              | N-ASF⁞ASM     |
| 045957   | Luk 21:11 | N-NPM              | N-NPM⁞NPF     |
| 046258   | Luk 21:31 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 049236   | Joh 1:9   | V-PNP-ASM          | V-PNP-ASM⁞NSN |
| 050688   | Joh 3:17  | V-PAS-3S           | V-PAS⁞AAS-3S  |
| 050951   | Joh 3:31  | A-GPN              | A-GPN⁞GPM     |
| 050973   | Joh 3:31  | A-GPN              | A-GPN⁞GPM     |
| 052654   | Joh 5:39  | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 053457   | Joh 6:39  | V-AAS-1S           | V-AAS⁞FAI-1S  |
| 055128   | Joh 8:16  | V-PAS-1S           | V-PAS⁞AAS-1S  |
| 055267   | Joh 8:23  | T-GPN              | T-GPN⁞GPM     |
| 055272   | Joh 8:23  | T-GPN              | T-GPN⁞GPM     |
| 058604   | Joh 12:19 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 059844   | Joh 14:1  | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 059851   | Joh 14:1  | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 060735   | Joh 15:18 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 060772   | Joh 15:20 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 061790   | Joh 17:15 | T-GSM              | T-GSM⁞GSN     |
| 061797   | Joh 17:15 | T-GSM              | T-GSM⁞GSN     |
| 066321   | Act 3:12  | D-DSN              | D-DSN⁞DSM     |
| 071398   | Act 10:28 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 071563   | Act 10:36 | A-GPM              | A-GPM⁞GPN     |
| 07490    | Mat 13:28 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 075568   | Act 16:37 | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 079686   | Act 23:5  | V-IAI-3S           | V-IAI⁞AAI-3S  |
| 081192   | Act 25:24 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 085139   | Rom 5:7   | A-GSM              | A-GSM⁞GSN     |
| 085145   | Rom 5:7   | A-GSM              | A-GSM⁞GSN     |
| 085394   | Rom 5:18  | A-GSN              | A-GSN⁞GSM     |
| 085404   | Rom 5:18  | A-GSN              | A-GSN⁞GSM     |
| 086768   | Rom 8:28  | A-APN              | A-APN⁞NPN     |
| 088057   | Rom 11:14 | V-FAI-1S           | V-FAI⁞AAS-1S  |
| 088062   | Rom 11:14 | V-FAI-1S           | V-FAI⁞AAS-1S  |
| 088635   | Rom 12:16 | T-DPM              | T-DPM⁞DPN     |
| 088636   | Rom 12:16 | A-DPM              | A-DPM⁞DPN     |
| 090732   | 1Co 1:26  | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 091068   | 1Co 2:13  | A-DPN              | A-DPN⁞DPM     |
| 092950   | 1Co 7:36  | A-NSF              | A-NSF⁞NSM     |
| 094554   | 1Co 11:24 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 095354   | 1Co 13:12 | N-ASN              | N-ASN⁞NSN     |
| 095378   | 1Co 13:13 | D-GPN              | D-GPN⁞GPF     |
| 099999   | 2Co 9:6   | D-ASN              | D-ASN⁞NSN     |
| 100496   | 2Co 11:1  | V-PMI-2P           | V-PMI⁞PMM-2P  |
| 102458   | Gal 3:7   | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 103687   | Gal 6:7   | V-PAS-3S           | V-PAS⁞AAS-3S  |
| 105014   | Eph 4:6   | A-GPM              | A-GPM⁞GPN     |
| 105017   | Eph 4:6   | A-GPM              | A-GPM⁞GPN     |
| 105020   | Eph 4:6   | A-GPM              | A-GPM⁞GPN     |
| 105496   | Eph 5:5   | V-RAM-2P           | V-RAM⁞RAI-2P  |
| 105687   | Eph 5:20  | A-GPN              | A-GPN⁞GPM     |
| 106998   | Php 2:15  | V-PEI-2P           | V-PEI⁞PEM-2P  |
| 108996   | Col 3:11  | A-DPN              | A-DPN⁞DPM     |
| 109852   | 1Th 2:9   | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 111572   | 2Th 3:3   | T-GSM              | T-GSM⁞GSN     |
| 116068   | Heb 2:11  | A-GSM              | A-GSM⁞GSN     |
| 117367   | Heb 7:4   | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 118918   | Heb 10:27 | N-NSM              | N-NSM⁞NSN     |
| 120005   | Heb 12:17 | V-RAI-2P           | V-RAI⁞RAM-2P  |
| 120232   | Heb 13:4  | A-DPM              | A-DPM⁞DPN     |
| 120546   | Heb 13:23 | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 122410   | 1Pe 1:6   | R-DSM              | R-DSM⁞DSN     |
| 122411   | 1Pe 1:6   | V-PNI-2P           | V-PNI⁞PNM-2P  |
| 122457   | 1Pe 1:8   | V-PNI-2P           | V-PNI⁞PNM-2P  |
| 122784   | 1Pe 2:5   | V-PPI-2P           | V-PPI⁞PPM-2P  |
| 124062   | 2Pe 1:4   | R-GPN              | R-GPN⁞GPF     |
| 124690   | 2Pe 2:19  | R-DSM              | R-DSM⁞DSN     |
| 124694   | 2Pe 2:19  | D-DSM              | D-DSM⁞DSN     |
| 125446   | 1Jo 2:8   | P-DSM              | P-DSM⁞DSN     |
| 125856   | 1Jo 2:27  | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 125884   | 1Jo 2:29  | V-PAI-2P           | V-PAI⁞PAM-2P  |
| 126387   | 1Jo 4:2   | V-PAI-2P           | V-PAI⁞PAM-2P  |


### 3.7) glosses modification
- remove all occurences of ’ (`2019`) and ”(`201D`)


### 3.7) text additions (not implemented yet, to-be-decided)

Mat 6:13【<RUBY><ruby><ruby>Ὅτι<rt>because</rt></ruby><rt>ὅτι</rt></ruby><rt>CONJ</rt></RUBY> <RUBY><ruby><ruby>σοῦ<rt>your</rt></ruby><rt>σύ</rt></ruby><rt>P-2GS</rt></RUBY> <RUBY><ruby><ruby><strong>ἐστιν</strong><rt>is</rt></ruby><rt>εἰμί</rt></ruby><rt>V-PAI-3S</rt></RUBY> <RUBY><ruby><ruby>ἡ<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-NSF</rt></RUBY> <RUBY><ruby><ruby>βασιλεία<rt>kingdom</rt></ruby><rt>βασιλεία</rt></ruby><rt>N-NSF</rt></RUBY> <RUBY><ruby><ruby>καὶ<rt>And</rt></ruby><rt>καί</rt></ruby><rt>CONJ</rt></RUBY> <RUBY><ruby><ruby>ἡ<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-NSF</rt></RUBY> <RUBY><ruby><ruby>δύναμις<rt>power</rt></ruby><rt>δύναμις</rt></ruby><rt>N-NSF</rt></RUBY> <RUBY><ruby><ruby>καὶ<rt>And</rt></ruby><rt>καί</rt></ruby><rt>CONJ</rt></RUBY> <RUBY><ruby><ruby>ἡ<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-NSF</rt></RUBY> <RUBY><ruby><ruby>δόξα<rt>glory</rt></ruby><rt>δόξα</rt></ruby><rt>N-NSF</rt></RUBY> <RUBY><ruby><ruby>εἰς<rt>into</rt></ruby><rt>εἰς</rt></ruby><rt>PREP</rt></RUBY> <RUBY><ruby><ruby>τοὺς<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-APM</rt></RUBY> <RUBY><ruby><ruby>αἰῶνας.<rt>age</rt></ruby><rt>αἰών</rt></ruby><rt>N-APM</rt></RUBY> </br><RUBY><ruby><ruby>Ἀμήν.<rt>Amen.</rt></ruby><rt>ἀμήν</rt></ruby><rt>HEB</rt></RUBY>】

---

## License :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OGNTa Project by Andley Chang is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/OpenGNT" rel="dct:source">https://github.com/eliranwong/OpenGNT</a>.

---

## Attribution :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Open Greek New Testament Project</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.



