# OGNTa (OpenGNT Abridged)

## Description

This is an abridged and updated version of [OpenGNTOGNT 3.3](https://github.com/eliranwong/OpenGNT). There are two main files:

**OGNTa.txt** = the main file of OGNTa Project, abridged and updated from OpenGNT_version3_3.csv ([BASE TEXT](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip))

**OGNTa-TC.txt** = OGNTa.txt with Traditional Chinese glosses adapted from [OpenGNT_interlinear_CUVtc.csv](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_interlinear_CUVtc.csv.zip)

## §1 Structure Changes

abridged to the following tab-separated columns:
-  OGNTsort = sort numbers of all words of the base text of OGNT.
-  Referemce = scripture Referemce in Book-Chapter:Verse format.
-  Greek = Greek text, combination of PMpWord/OGNTa/PMfWord, where:
   - PMpWord = punctuation mark(s) preceding the main word with `<strong>` tags enclosed;
     - `[[` changed to `⟦`
     - `]]` changed to `⟧`
   - OGNTa = Greek word of OGNT in accented form;
   - PMfWord = punctuation mark(s) following the main word with `<strong>` tags enclosed.
-  Lemma = Greek word of OGNT in lexical form.
-  Code  = Morphological Analysis Codes.
-  IT = context-sensitive English glossess (from Berean Interlinear Bible)
-  TC = context-sensitive Chinese glossess, within which:
  - `⸂`/`⸃` mark the beginning/ending of additional CUV text that are not aligned to the Lemma

For example :
| OGNTsort | Referemce | Greek       | Lemma   | Code    | IT/TC         |
| -------- | --------- | ----------- | ------- | ------- | ------------- |
| 000001   | Mat 1:1   | Βίβλος      | βίβλος  | N-NSF   | [The] book    |
| 000172   | 太 1:11   | Βαβυλῶνος.¶ | Βαβυλών | N-GSF-L | 巴比倫⸂的時候 |
| 000382   | Mat 1:23  | ¬Ἰδοὺ       | ἰδού    | INJ     | look!         |
| 029617   | Mar 16:20 | ⟦πάντα      | πᾶς     | A-APN   | all           |


## §2 Content Changes
### §2.1 Text Additions

```

002730a	Mat 6:13	⟦ὅτι	ὅτι	CONJ	that/since
002730b	Mat 6:13	σοῦ	σύ	P-2GS	you
002730c	Mat 6:13	ἐστιν	εἰμί	V-PAI-3S	to be
002730d	Mat 6:13	ἡ	ὁ	T-NSF	the/this/who
002730e	Mat 6:13	βασιλεία	βασιλεία	N-NSF	kingdom
002730f	Mat 6:13	καὶ	καί	CONJ	and
002730g	Mat 6:13	ἡ	ὁ	T-NSF	the/this/who
002730h	Mat 6:13	δύναμις	δύναμις	N-NSF	power
002730i	Mat 6:13	καὶ	καί	CONJ	and
002730j	Mat 6:13	ἡ	ὁ	T-NSF	the/this/who
002730k	Mat 6:13	δόξα	δόξα	N-NSF	glory
002730l	Mat 6:13	εἰς	εἰς	PREP	toward
002730m	Mat 6:13	τοῦς	ὁ	T-APM	the/this/who
002730n	Mat 6:13	αἰῶνας	αἰών	N-APM	an age
002730o	Mat 6:13	ἀμήν.⟧¶	ἀμήν	INJ-HEB	amen

```

### §2.2 Lemma Modifications

| OpenGNT_version3_3   | OGNTa |
| -------------------- | ----- |
| Δαυείδ, Δαυίδ, Δαβίδ | Δαυίδ |
| γε μή(γε)            | γε γε |
| μή μή(γε)            | μή μή |
| ἔπω, ἐρῶ, εἶπον      | εἶπον |
| ὅς, ἥ                | ὅς    |
| ὅστις, ἥτις          | ὅστις |
| ὕδωρ, ὕδατος         | ὕδωρ  |

### §2.3 Code Modifications

#### §2.3.1 General Modifications
- Part of Speech:
  - αὐστηρός: P → A
  - ἄρα: CONJ → PRT
  - ἐγγύς: PREP → ADV
  - ὅτι: ADV → CONJ
  - ὅπου: ADV → CONJ
  - γε: PRT-N → PRT
- Nouns:
  - remove -P, -L. -T, -C after Case-Number-Gender
-  Adjectives
   - remove -C, -S, -N, -L, -PG, -T, -P after Case-Number-Gender
- Verbs: 
  - Secondary Tense-Forms:
    - Second Present: 2P → P
    - Second Aorist: 2A → A
    - Second Future: 2F → F
    - Second Perfect: 2R → R
    - Second Pluperfect: 2L → L
  - Voice System: (M, P remain unchanged)
    - Middle Deponent: D → M 
    - Middle or passive Deponent: N → M
    - Either middle or passive: E → M
    - Passive Deponent: O → P
- Glosses:    
  - remove all occurences of ’ (UNICODE `2019`) and ”(UNICODE `201D`)


#### §2.3.2 Specific Modifications

| OGNTsort | Referemce | OpenGNT_version3_3 | OGNTa       |
| -------- | --------- | ------------------ | ----------- |
| 018408   | Mar 1:5   | N-NSF-L            | A-NSF       |
| 019639   | Mar 3:4   |                    | good        |
| 021935   | Mar 6:23  |                    | which       |
| 107119   | Php 2:25  | A-NSN              | A-ASN       |
| 122411   | 1Pe 1:6   | ἀγαλλιᾶσθε         | ἀγαλλιᾶσθε, |


#### §2.3.4 Code Enhancements

| OGNTsort | Referemce | OpenGNT_version3_3 | OGNTa         |
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
| 043789   | Luk 18:8  | CONJ               | PRT-I         |
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
| 069974   | Act 8:30  | CONJ               | PRT-I         |
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
| 102313   | Gal 2:17  | CONJ               | PRT-I         |
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






---

## License :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OGNTa Project by Andley Chang is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/OpenGNT" rel="dct:source">https://github.com/eliranwong/OpenGNT</a>.

---

## Attribution :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Open Greek New Testament Project</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.



