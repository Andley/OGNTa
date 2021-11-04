# OGNTa (OpenGNT Abridged)

This is an abridged and updated version of OpenGNT (OGNT 3.3 [Base Text](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip)) 

**OGNTa.txt** = the main file of OGNTa Project, abridged and updated from OpenGNT_version3_3.csv

**OGNTa-TC.txt** = OGNTa.txt with Traditional Chinese glosses adapted from [Chinese Standard Bible NT](https://github.com/eliranwong/OpenGNT/blob/master/mapping_CSB/OGNTtoCSB_DB_Export_version_2.xlsx.zip)

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

- TC = Traditional Chinese gloss

| OGNTsort | referemce | Greek | lexeme | rmac  | TBESG  | IT/TC |
|----------|-----------|-------|--------|-------|--------|----|
| 000001   | Mat 1:1   | Βίβλος  | βίβλος | N-NSF | book | [The] book |
| 029616   | Mar 16:20 | σημείων . ⟧ ¶	| σημεῖον | N-GPN | sign | signs.|
| 029617   | Mar 16:20 | ⟦ πάντα | πᾶς	| A-APN	| all | all |
| 000382 |Mat 1:23 | ¬Ἰδοὺ | ἰδού | INJ | look! | 看 |


## Content Changes

### rmac enhancements
- OGNTsort	reference	Greek : `rmac-old` ⇒ `rmac-new`
- 001339	Mat 4:7	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 001446	Mat 4:15	¬Γῆ : `N-NSF` ⇒ `N-NSF⁞VSF`
- 001449	Mat 4:15	γῆ : `N-NSF` ⇒ `N-NSF⁞VSF`
- 001456	Mat 4:15	¬Γαλιλαία : `N-NSF-L` ⇒ `N-NSF⁞VSF-L`
- 002311	Mat 5:37	τούτων : `D-GPN` ⇒ `D-GPN⁞GPM`
- 002313	Mat 5:37	τοῦ : `T-GSM` ⇒ `T-GSM⁞GSN`
- 002314	Mat 5:37	πονηροῦ : `A-GSM` ⇒ `A-GSM⁞GSN`
- 002332	Mat 5:39	τῷ : `T-DSN` ⇒ `T-DSN⁞DSM`
- 002729	Mat 6:13	τοῦ : `T-GSN` ⇒ `T-GSM⁞GSN`
- 018408	Mar 1:5	Ἰουδαία : `N-NSF-L` ⇒ `A-NSF-L`
- 044656	Luk 19:21	αὐστηρὸς : `P-NSM` ⇒ `A-NSM`
- 044681	Luk 19:22	αὐστηρός : `P-NSM` ⇒ `A-NSM`
- 07490	Mat 13:28	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 010230	Mat 17:26	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 011277	Mat 19:21	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 012521	Mat 21:27	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 013408	Mat 22:37	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 014321	Mat 24:7	λιμοὶ : `N-NPM` ⇒ `N-NPM⁞NPF`
- 014722	Mat 24:33	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 014870	Mat 24:43	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 015295	Mat 25:21	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 015338	Mat 25:23	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 015856	Mat 26:7	ἀλάβαστρον : `N-ASN` ⇒ `A-ASM⁞ASF⁞ASN`
- 016276	Mat 26:34	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 017996	Mat 27:65	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 023937	Mar 9:12	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 024376	Mar 9:38	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 024873	Mar 10:20	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 025028	Mar 10:29	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 026430	Mar 12:24	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 027324	Mar 13:29	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 027922	Mar 14:29	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 030929	Luk 2:7	ἀνέκλινεν : `V-AAI-3S` ⇒ `V-AAI⁞IAI-3S`
- 061790	Joh 17:15	τοῦ : `T-GSM` ⇒ `T-GSM⁞GSN`
- 061797	Joh 17:15	τοῦ : `T-GSM` ⇒ `T-GSM⁞GSN`
- 111572	2Th 3:3	τοῦ : `T-GSM` ⇒ `T-GSM⁞GSN`
- 058604	Joh 12:19	Θεωρεῖτε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 059844	Joh 14:1	πιστεύετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 059851	Joh 14:1	πιστεύετε. : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 060735	Joh 15:18	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 060772	Joh 15:20	Μνημονεύετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 040274	Luk 12:39	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 046258	Luk 21:31	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 052654	Joh 5:39	Ἐραυνᾶτε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 081192	Act 25:24	θεωρεῖτε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 090732	1Co 1:26	Βλέπετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 094554	1Co 11:24	ποιεῖτε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 102458	Gal 3:7	Γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 109852	1Th 2:9	Μνημονεύετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 117367	Heb 7:4	Θεωρεῖτε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 120546	Heb 13:23	Γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 125856	1Jo 2:27	μένετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 125884	1Jo 2:29	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 126387	1Jo 4:2	γινώσκετε : `V-PAI-2P` ⇒ `V-PAI⁞PAM-2P`
- 071398	Act 10:28	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 075568	Act 16:37	ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 079686	Act 23:5	Ἔφη : `V-IAI-3S` ⇒ `V-IAI⁞AAI-3S`
- 044497	Luk 19:11	ἐγγὺς : `PREP` ⇒ `ADV`
- 122411	1Pe 1:6	ἀγαλλιᾶσθε : `V-PNI-2P` ⇒ `V-PNI⁞PNM-2P`
- 122457	1Pe 1:8	ἀγαλλιᾶσθε : `V-PNI-2P` ⇒ `V-PNI⁞PNM-2P`
- 122784	1Pe 2:5	οἰκοδομεῖσθε : `V-PPI-2P` ⇒ `V-PPI⁞PPM-2P`
- 044085	Luk 18:25	κάμηλον : `N-ASF` ⇒ `N-ASF⁞ASM`
- 045957	Luk 21:11	λιμοὶ : `N-NPM` ⇒ `N-NPM⁞NPF`
- 049236	Joh 1:9	ἐρχόμενον : `V-PNP-ASM` ⇒ `V-PNP-ASM⁞NSN`
- 050688	Joh 3:17	κρίνῃ : `V-PAS-3S` ⇒ `V-PAS⁞AAS-3S`
- 050951	Joh 3:31	πάντων : `A-GPN` ⇒ `A-GPN⁞GPM`
- 050973	Joh 3:31	πάντων : `A-GPN` ⇒ `A-GPN⁞GPM`
- 053457	Joh 6:39	ἀναστήσω : `V-AAS-1S` ⇒ `V-AAS⁞FAI-1S`
- 105014	Eph 4:6	πάντων, : `A-GPM` ⇒ `A-GPM⁞GPN`
- 105017	Eph 4:6	πάντων : `A-GPM` ⇒ `A-GPM⁞GPN`
- 105020	Eph 4:6	πάντων : `A-GPM` ⇒ `A-GPM⁞GPN`
- 055128	Joh 8:16	κρίνω : `V-PAS-1S` ⇒ `V-PAS⁞AAS-1S`
- 055267	Joh 8:23	τῶν : `T-GPN` ⇒ `T-GPN⁞GPM`
- 055272	Joh 8:23	τῶν : `T-GPN` ⇒ `T-GPN⁞GPM`
- 066321	Act 3:12	τούτῳ : `D-DSN` ⇒ `D-DSN⁞DSM`
- 085145	Rom 5:7	ἀγαθοῦ : `A-GSM` ⇒ `A-GSM⁞GSN`
- 085139	Rom 5:7	δικαίου : `A-GSM` ⇒ `A-GSM⁞GSN`
- 071563	Act 10:36	πάντων : `A-GPM` ⇒ `A-GPM⁞GPN`
- 085394	Rom 5:18	ἑνὸς : `A-GSN` ⇒ `A-GSN⁞GSM`
- 085404	Rom 5:18	ἑνὸς : `A-GSN` ⇒ `A-GSN⁞GSM`
- 086768	Rom 8:28	πάντα : `A-APN` ⇒ `A-APN⁞NPN`
- 125446	1Jo 2:8	αὐτῷ : `P-DSM` ⇒ `P-DSM⁞DSN`
- 124694	2Pe 2:19	τούτῳ : `D-DSM` ⇒ `D-DSM⁞DSN`
- 124690	2Pe 2:19	ᾧ : `R-DSM` ⇒ `R-DSM⁞DSN`
- 124062	2Pe 1:4	ὧν : `R-GPN` ⇒ `R-GPN⁞GPF`
- 122410	1Pe 1:6	ᾧ : `R-DSM` ⇒ `R-DSM⁞DSN`
- 120232	Heb 13:4	πᾶσιν : `A-DPM` ⇒ `A-DPM⁞DPN`
- 120005	Heb 12:17	ἴστε : `V-RAI-2P` ⇒ `V-RAI⁞RAM-2P`
- 118918	Heb 10:27	ζῆλος : `N-NSM` ⇒ `N-NSM⁞NSN`
- 116068	Heb 2:11	ἑνὸς : `A-GSM` ⇒ `A-GSM⁞GSN`
- 108996	Col 3:11	πᾶσιν : `A-DPN` ⇒ `A-DPN⁞DPM`
- 105687	Eph 5:20	πάντων : `A-GPN` ⇒ `A-GPN⁞GPM`
- 105496	Eph 5:5	ἴστε : `V-RAM-2P` ⇒ `V-RAM⁞RAI-2P`
- 103687	Gal 6:7	σπείρῃ : `V-PAS-3S` ⇒ `V-PAS⁞AAS-3S`
- 100496	2Co 11:1	ἀνέχεσθέ : `V-PMI-2P` ⇒ `V-PMI⁞PMM-2P`
- 099999	2Co 9:6	Τοῦτο : `D-ASN` ⇒ `D-ASN⁞NSN`
- 095378	1Co 13:13	τούτων : `D-GPN` ⇒ `D-GPN⁞GPF`
- 095354	1Co 13:12	πρόσωπον· : `N-ASN` ⇒ `N-ASN⁞NSN`
- 092950	1Co 7:36	ὑπέρακμος : `A-NSF` ⇒ `A-NSF⁞NSM`
- 091068	1Co 2:13	πνευματικοῖς : `A-DPN` ⇒ `A-DPN⁞DPM`
- 088635	Rom 12:16	τοῖς : `T-DPM` ⇒ `T-DPM⁞DPN`
- 088636	Rom 12:16	ταπεινοῖς : `A-DPM` ⇒ `A-DPM⁞DPN`
- 088062	Rom 11:14	σώσω : `V-FAI-1S` ⇒ `V-FAI⁞AAS-1S`
- 088057	Rom 11:14	παραζηλώσω : `V-FAI-1S` ⇒ `V-FAI⁞AAS-1S`

---

## License :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OGNTa Project by Andley Chang is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/OpenGNT" rel="dct:source">https://github.com/eliranwong/OpenGNT</a>.

---

## Attribution :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Open Greek New Testament Project</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.



