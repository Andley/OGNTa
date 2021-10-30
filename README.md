# OGNTa (OpenGNT Abridged)

This is an abridged and updated version of OpenGNT (OGNT 3.3 [Base Text](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip)) 

**OGNTa.txt** = the main file of OGNTa Project, abridged and updated from OpenGNT_version3_3.csv

**OGNTa-TC.txt** = OGNTa.txt with Chinese glosses adapted from [Chinese Standard Bible NT](https://github.com/eliranwong/OpenGNT/blob/master/mapping_CSB/OGNTtoCSB_DB_Export_version_2.xlsx.zip)

## Structure Changes

OGNT3.3 abridged to the following tab-separated columns:
-  OGNTsort = sort numbers of all words of the base text of OGNT.
-  reference = scripture reference in Book-Chapter:Verse format.
-  Greek = Greek text, comprised of PMpWord/OGNTa/PMfWord, where:
   - PMpWord = punctuation mark(s) preceding the main word.
     - [[ changed to ⟦
     - ]] changed to ⟧
   - OGNTa = Greek word of OGNT in accented form.
   - PMfWord = punctuation mark(s) following the main word.
-  lexeme = Greek word of OGNT in lexical form.
-  rmac = Robinson's Morphological Analysis Codes.
-  TBESG = context-insensitive glosses (from Tyndale House's TAGNT).
-  IT = context-sensitive glossess (from Berean Interlinear Bible)


| OGNTsort | referemce | Greek | lexeme | rmac  | TBESG  | IT |
|----------|-----------|-------|--------|-------|--------|----|
| 000001   | Mat 1:1   | Βίβλος  | βίβλος | N-NSF | book | [The] book |
| 029616   | Mar 16:20 | σημείων . ⟧ ¶	| σημεῖον | N-GPN | sign | signs.|
| 029617   | Mar 16:20 | ⟦ πάντα | πᾶς	| A-APN	| all | all |

## Content Changes
OGNTsort	reference	Greek :	`rmac-old`	⇒	`rmac-new`

### rmac corrections
- 018408	Mar 1:5	Ἰουδαία :	`N-NSF-L`	⇒	`A-NSF-L`
- 044497	Luk 19:11	ἐγγὺς :	`PREP`	⇒	`ADV`
- 044656	Luk 19:21	αὐστηρὸς :	`P-NSM`	⇒	`A-NSM`
- 044681	Luk 19:22	αὐστηρός :	`P-NSM`	⇒	`A-NSM`

### rmac enhancements
- 001339	Mat 4:7	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 001446	Mat 4:15	¬Γῆ :	`N-NSF`	⇒	`N-N⁞VSF`
- 001449	Mat 4:15	γῆ :	`N-NSF`	⇒	`N-N⁞VSF`
- 001456	Mat 4:15	¬Γαλιλαία :	`N-NSF-L`	⇒	`N-N⁞VSF-L`
- 002311	Mat 5:37	τούτων :	`D-GPN`	⇒	`D-GPN⁞M`
- 002313	Mat 5:37	τοῦ :	`T-GSM`	⇒	`T-GSM⁞N`
- 002314	Mat 5:37	πονηροῦ :	`A-GSM`	⇒	`A-GSM⁞N`
- 002332	Mat 5:39	τῷ :	`T-DSN`	⇒	`T-DSN⁞M`
- 002729	Mat 6:13	τοῦ :	`T-GSN`	⇒	`T-GSM⁞N`
- 07490	Mat 13:28	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 010230	Mat 17:26	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 011277	Mat 19:21	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 012521	Mat 21:27	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 013408	Mat 22:37	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 014321	Mat 24:7	λιμοὶ :	`N-NPM`	⇒	`N-NPM⁞F`
- 014722	Mat 24:33	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 014870	Mat 24:43	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 015295	Mat 25:21	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 015338	Mat 25:23	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 015856	Mat 26:7	ἀλάβαστρον :	`N-ASN`	⇒	`A-ASM⁞F⁞N`
- 016276	Mat 26:34	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 017996	Mat 27:65	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 023937	Mar 9:12	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 024376	Mar 9:38	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 024873	Mar 10:20	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 025028	Mar 10:29	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 026430	Mar 12:24	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 027324	Mar 13:29	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 027922	Mar 14:29	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 030929	Luk 2:7	ἀνέκλινεν :	`V-AAI-3S`	⇒	`V-A⁞IAI-3S`
- 061790	Joh 17:15	τοῦ :	`T-GSM`	⇒	`T-GSM⁞N`
- 061797	Joh 17:15	τοῦ :	`T-GSM`	⇒	`T-GSM⁞N`
- 111572	2Th 3:3	τοῦ :	`T-GSM`	⇒	`T-GSM⁞N`
- 058604	Joh 12:19	Θεωρεῖτε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 059844	Joh 14:1	πιστεύετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 059851	Joh 14:1	πιστεύετε. :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 060735	Joh 15:18	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 060772	Joh 15:20	Μνημονεύετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 040274	Luk 12:39	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 046258	Luk 21:31	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 052654	Joh 5:39	Ἐραυνᾶτε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 081192	Act 25:24	θεωρεῖτε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 090732	1Co 1:26	Βλέπετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 094554	1Co 11:24	ποιεῖτε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 102458	Gal 3:7	Γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 109852	1Th 2:9	Μνημονεύετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 117367	Heb 7:4	Θεωρεῖτε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 120546	Heb 13:23	Γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 125856	1Jo 2:27	μένετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 125884	1Jo 2:29	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 126387	1Jo 4:2	γινώσκετε :	`V-PAI-2P`	⇒	`V-PAI⁞M-2P`
- 071398	Act 10:28	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 075568	Act 16:37	ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`
- 079686	Act 23:5	Ἔφη :	`V-IAI-3S`	⇒	`V-I⁞AAI-3S`




---

## License :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OGNTa Project by Andley Chang is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/OpenGNT" rel="dct:source">https://github.com/eliranwong/OpenGNT</a>.

---

## Attribution :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Open Greek New Testament Project</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.



