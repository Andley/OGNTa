# OGNTa (OpenGNT Abridged)

This is an abridged and updated version of OpenGNT (OGNT 3.3 [Base Text](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip)) 

**OGNTa.txt** = the main file of OGNTa Project, abridged and updated from OpenGNT_version3_3.csv

**OGNTa-TC.txt** = with Traditional Chinese glosses adapted from [OpenGNT_interlinear_CUVtc.csv](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_interlinear_CUVtc.csv.zip)

## Structure Changes

OGNT3.3 abridged to the following tab-separated columns:
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
-  TBESG = context-insensitive glosses (from Tyndale House's TAGNT).
-  IT = context-sensitive English glossess (from Berean Interlinear Bible)
-  TC = context-sensitive Chinese glossess, within which
  - `⸂`/`⸃` mark the beginning/ending of additional CUV text that are not aligned to the lemma


| OGNTsort | referemce | Greek | lemma | rmac  | TBESG  | IT/TC |
|----------|-----------|-------|--------|-------|--------|----|
| 000001   | Mat 1:1   | Βίβλος  | βίβλος | N-NSF | book | [The] book |
| 029616   | Mar 16:20 | σημείων . ⟧ ¶	| σημεῖον | N-GPN | sign | signs.|
| 029617   | Mar 16:20 | ⟦ πάντα | πᾶς	| A-APN	| all | all |
| 000382 |Mat 1:23 | ¬Ἰδοὺ | ἰδού | INJ | look! | 看 |


## Content Changes

### text additions
Mat 6:13【<RUBY><ruby><ruby>Ὅτι<rt>because</rt></ruby><rt>ὅτι</rt></ruby><rt>CONJ</rt></RUBY> <RUBY><ruby><ruby>σοῦ<rt>your</rt></ruby><rt>σύ</rt></ruby><rt>P-2GS</rt></RUBY> <RUBY><ruby><ruby><strong>ἐστιν</strong><rt>is</rt></ruby><rt>εἰμί</rt></ruby><rt>V-PAI-3S</rt></RUBY> <RUBY><ruby><ruby>ἡ<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-NSF</rt></RUBY> <RUBY><ruby><ruby>βασιλεία<rt>kingdom</rt></ruby><rt>βασιλεία</rt></ruby><rt>N-NSF</rt></RUBY> <RUBY><ruby><ruby>καὶ<rt>And</rt></ruby><rt>καί</rt></ruby><rt>CONJ</rt></RUBY> <RUBY><ruby><ruby>ἡ<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-NSF</rt></RUBY> <RUBY><ruby><ruby>δύναμις<rt>power</rt></ruby><rt>δύναμις</rt></ruby><rt>N-NSF</rt></RUBY> <RUBY><ruby><ruby>καὶ<rt>And</rt></ruby><rt>καί</rt></ruby><rt>CONJ</rt></RUBY> <RUBY><ruby><ruby>ἡ<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-NSF</rt></RUBY> <RUBY><ruby><ruby>δόξα<rt>glory</rt></ruby><rt>δόξα</rt></ruby><rt>N-NSF</rt></RUBY> <RUBY><ruby><ruby>εἰς<rt>into</rt></ruby><rt>εἰς</rt></ruby><rt>PREP</rt></RUBY> <RUBY><ruby><ruby>τοὺς<rt>the</rt></ruby><rt>ὁ</rt></ruby><rt>T-APM</rt></RUBY> <RUBY><ruby><ruby>αἰῶνας.<rt>age</rt></ruby><rt>αἰών</rt></ruby><rt>N-APM</rt></RUBY> </br><RUBY><ruby><ruby>Ἀμήν.<rt>Amen.</rt></ruby><rt>ἀμήν</rt></ruby><rt>HEB</rt></RUBY>】+

### punctuation mark changes
- 122411	1Pe 1:6	ἀγαλλιᾶσθε : `ἀγαλλιᾶσθε` ⇒ `ἀγαλλιᾶσθε ,` 


### punctuation mark changes
- 122411	1Pe 1:6	ἀγαλλιᾶσθε : `ἀγαλλιᾶσθε` ⇒ `ἀγαλλιᾶσθε ,` 


### rmac enhancements
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
- 106998	Php 2:15	φαίνεσθε :`V-PEI-2P` ⇒ `V-PEI⁞PEM-2P`
- 107119	Php 2:25	Ἀναγκαῖον :`A-NSN` ⇒ `A-ASN`
- 030349	Luk 1:43	ἵνα	:`ADV` ⇒ `CONJ`
- 053269	Joh 6:29	ἵνα	:`ADV` ⇒ `CONJ`
- 053447	Joh 6:39	ἵνα	:`ADV` ⇒ `CONJ`
- 053471	Joh 6:40	ἵνα	:`ADV` ⇒ `CONJ`
- 058273	Joh 11:57	ἵνα	:`ADV` ⇒ `CONJ`
- 059756	Joh 13:34	ἵνα	:`ADV` ⇒ `CONJ`
- 059762	Joh 13:34	ἵνα	:`ADV` ⇒ `CONJ`
- 060562	Joh 15:8	ἵνα	:`ADV` ⇒ `CONJ`
- 060630	Joh 15:12	ἵνα	:`ADV` ⇒ `CONJ`
- 060727	Joh 15:17	ἵνα	:`ADV` ⇒ `CONJ`
- 061545	Joh 17:3	ἵνα	:`ADV` ⇒ `CONJ`
- 061569	Joh 17:4	ἵνα	:`ADV` ⇒ `CONJ`
- 062758	Joh 18:39	ἵνα	:`ADV` ⇒ `CONJ`
- 075931	Act 17:15	ἵνα	:`ADV` ⇒ `CONJ`
- 089866	Rom 15:31	ἵνα	:`ADV` ⇒ `CONJ`
- 106424	Php 1:9	ἵνα	:`ADV` ⇒ `CONJ`
- 109400	Col 4:12	ἵνα	:`ADV` ⇒ `CONJ`
- 112077	1Ti 1:18	ἵνα	:`ADV` ⇒ `CONJ`
- 126106	1Jo 3:11	ἵνα	:`ADV` ⇒ `CONJ`
- 126321	1Jo 3:23	ἵνα	:`ADV` ⇒ `CONJ`
- 126803	1Jo 4:21	ἵνα	:`ADV` ⇒ `CONJ`
- 126862	1Jo 5:3	ἵνα	:`ADV` ⇒ `CONJ`
- 127342	2Jo 1:6	ἵνα	:`ADV` ⇒ `CONJ`
- 127356	2Jo 1:6	ἵνα	:`ADV` ⇒ `CONJ`
- 127530	3Jo 1:4	ἵνα	:`ADV` ⇒ `CONJ`
- 016647	Mat 26:54	ὅτι : `ADV` ⇒ `CONJ`
- 019328	Mar 2:16	Ὅτι : `ADV` ⇒ `CONJ`
- 023926	Mar 9:11	Ὅτι : `ADV` ⇒ `CONJ`
- 024224	Mar 9:28	Ὅτι : `ADV` ⇒ `CONJ`
- 025128	Mar 10:33	ὅτι : `ADV` ⇒ `CONJ`
- 033721	Luk 5:36	ὅτι : `ADV` ⇒ `CONJ`
- 038041	Luk 10:11	ὅτι : `ADV` ⇒ `CONJ`
- 038188	Luk 10:20	ὅτι : `ADV` ⇒ `CONJ`
- 040275	Luk 12:39	ὅτι : `ADV` ⇒ `CONJ`
- 047331	Luk 22:61	ὅτι : `ADV` ⇒ `CONJ`
- 048999	Luk 24:44	ὅτι : `ADV` ⇒ `CONJ`
- 051666	Joh 4:37	ὅτι : `ADV` ⇒ `CONJ`
- 056390	Joh 9:25	ὅτι : `ADV` ⇒ `CONJ`
- 056465	Joh 9:30	ὅτι : `ADV` ⇒ `CONJ`
- 060880	Joh 15:25	ὅτι : `ADV` ⇒ `CONJ`
- 062139	Joh 18:9	ὅτι : `ADV` ⇒ `CONJ`
- 063761	Joh 20:9	ὅτι : `ADV` ⇒ `CONJ`
- 064700	Joh 21:23	ὅτι : `ADV` ⇒ `CONJ`
- 075553	Act 16:36	ὅτι : `ADV` ⇒ `CONJ`
- 078184	Act 20:35	ὅτι : `ADV` ⇒ `CONJ`
- 078198	Act 20:35	ὅτι : `ADV` ⇒ `CONJ`
- 078239	Act 20:38	ὅτι : `ADV` ⇒ `CONJ`
- 078863	Act 21:31	ὅτι : `ADV` ⇒ `CONJ`
- 080479	Act 24:14	ὅτι : `ADV` ⇒ `CONJ`
- 080603	Act 24:21	ὅτι : `ADV` ⇒ `CONJ`
- 083101	Act 28:25	ὅτι : `ADV` ⇒ `CONJ`
- 083744	Rom 1:32	ὅτι : `ADV` ⇒ `CONJ`
- 083812	Rom 2:3	ὅτι : `ADV` ⇒ `CONJ`
- 085551	Rom 6:6	ὅτι : `ADV` ⇒ `CONJ`
- 086230	Rom 7:21	ὅτι : `ADV` ⇒ `CONJ`
- 086976	Rom 9:2	ὅτι : `ADV` ⇒ `CONJ`
- 087050	Rom 9:6	ὅτι : `ADV` ⇒ `CONJ`
- 087551	Rom 10:5	ὅτι : `ADV` ⇒ `CONJ`
- 088251	Rom 11:25	ὅτι : `ADV` ⇒ `CONJ`
- 088917	Rom 13:11	ὅτι : `ADV` ⇒ `CONJ`
- 090521	1Co 1:12	ὅτι : `ADV` ⇒ `CONJ`
- 090738	1Co 1:26	ὅτι : `ADV` ⇒ `CONJ`
- 092764	1Co 7:26	ὅτι : `ADV` ⇒ `CONJ`
- 094529	1Co 11:23	ὅτι : `ADV` ⇒ `CONJ`
- 096028	1Co 15:3	ὅτι : `ADV` ⇒ `CONJ`
- 096039	1Co 15:4	ὅτι : `ADV` ⇒ `CONJ`
- 096042	1Co 15:4	ὅτι : `ADV` ⇒ `CONJ`
- 096052	1Co 15:5	ὅτι : `ADV` ⇒ `CONJ`
- 096692	1Co 15:50	ὅτι : `ADV` ⇒ `CONJ`
- 098757	2Co 5:14	ὅτι : `ADV` ⇒ `CONJ`
- 099629	2Co 8:9	ὅτι : `ADV` ⇒ `CONJ`
- 099918	2Co 9:2	ὅτι : `ADV` ⇒ `CONJ`
- 100292	2Co 10:7	ὅτι : `ADV` ⇒ `CONJ`
- 100354	2Co 10:11	ὅτι : `ADV` ⇒ `CONJ`
- 100649	2Co 11:10	ὅτι : `ADV` ⇒ `CONJ`
- 101833	Gal 1:13	ὅτι : `ADV` ⇒ `CONJ`
- 105498	Eph 5:5	ὅτι : `ADV` ⇒ `CONJ`
- 106359	Php 1:6	ὅτι : `ADV` ⇒ `CONJ`
- 106596	Php 1:20	ὅτι : `ADV` ⇒ `CONJ`
- 106726	Php 1:27	ὅτι : `ADV` ⇒ `CONJ`
- 107012	Php 2:16	ὅτι : `ADV` ⇒ `CONJ`
- 107088	Php 2:22	ὅτι : `ADV` ⇒ `CONJ`
- 110591	1Th 4:15	ὅτι : `ADV` ⇒ `CONJ`
- 111689	2Th 3:10	ὅτι : `ADV` ⇒ `CONJ`
- 111912	1Ti 1:9	ὅτι : `ADV` ⇒ `CONJ`
- 112009	1Ti 1:15	ὅτι : `ADV` ⇒ `CONJ`
- 113652	2Ti 1:15	ὅτι : `ADV` ⇒ `CONJ`
- 114072	2Ti 3:1	ὅτι : `ADV` ⇒ `CONJ`
- 122152	Jas 5:11	ὅτι : `ADV` ⇒ `CONJ`
- 124363	2Pe 1:20	ὅτι : `ADV` ⇒ `CONJ`
- 124797	2Pe 3:3	ὅτι : `ADV` ⇒ `CONJ`
- 124838	2Pe 3:5	ὅτι : `ADV` ⇒ `CONJ`
- 124891	2Pe 3:8	ὅτι : `ADV` ⇒ `CONJ`
- 125200	1Jo 1:5	ὅτι : `ADV` ⇒ `CONJ`
- 126568	1Jo 4:10	ὅτι : `ADV` ⇒ `CONJ`
- 126574	1Jo 4:10	ὅτι : `ADV` ⇒ `CONJ`
- 127033	1Jo 5:11	ὅτι : `ADV` ⇒ `CONJ`
- 127094	1Jo 5:14	ὅτι : `ADV` ⇒ `CONJ`
- 128743	Rev 2:6	ὅτι : `ADV` ⇒ `CONJ`
- 129279	Rev 3:1	ὅτι : `ADV` ⇒ `CONJ`
- 129282	Rev 3:1	ὅτι : `ADV` ⇒ `CONJ`
- 129619	Rev 3:15	ὅτι : `ADV` ⇒ `CONJ`

---

## License :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OGNTa Project by Andley Chang is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/OpenGNT" rel="dct:source">https://github.com/eliranwong/OpenGNT</a>.

---

## Attribution :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Open Greek New Testament Project</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.



