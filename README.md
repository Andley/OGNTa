# OGNTa (OpenGNT Abridged)

This is an abridged and updated version of OpenGNT Version 3 [OGNT 3.3 Base Text](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip)

## Structure changes

-  OGNT3.3 abridged to the following tab-separated columns:
   -  OGNTsort = sort numbers of all words of the base text of OGNT.
   -  Book = Book number, ranging from 40 to 66.
   -  Chapter = Chapter number.
   -  Verse = verse number.
   -  OGNT = Greek word of OGNT in accented form.
   -  Lemma = Greek word of OGNT in lexical form.
   -  RMAC = Robinson's Morphological Analysis Codes.
   -  TBESG = context-insensitive glosses (from Tyndale House's TAGNT).
   -  IT = context-sensitive glossess (from Berean Interlinear Bible)
   -  PMpWord = punctuation mark(s) preceding the main word.
      -  [[ changed to ⟦
      -  ]] changed to ⟧
   -  PMfWord = punctuation mark(s) following the main word.


| OGNTsort | Book | Chapter | Verse | OGNTa    | lexeme   | rmac       | TBESG    | IT           | PMpWord | PMfWord |
|----------|------|---------|-------|----------|----------|------------|----------|--------------|:-------:|:-------:|
| 000001   | 40   | 1       | 1     | Βίβλος   | βίβλος   | N-NSF      | book     | [The] book   |         |         |
| 000008   | 40   | 1       | 1     | Ἀβραάμ   | Ἀβραάμ   | N-GSM-P    | Abraham  | of Abraham:  |         | .¶      |
| 029446   | 41   | 16      | 9     | Ἀναστὰς  | ἀνίστημι | V-2AAP-NSM | to arise | Having risen | ⟦       |         |


## Content changes
- `018408	41	1	5	Ἰουδαία	Ἰουδαία	N-NSF-L	Judea	of Judea		` ⇒ `A-NSF-L`
- `044656	42	19	21	αὐστηρὸς	αὐστηρός	P-NSM	severe	harsh		` ⇒ `A-NSM`
- `044681	42	19	22	αὐστηρός	αὐστηρός	P-NSM	severe	harsh		` ⇒ `A-NSM`
- `qqq` is a dood `aaa`


---

## License :

The entire text of OGNTa is released under the following license:


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OGNTa is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

---

## Attribution :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Open Greek New Testament Project</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/OpenGNT" rel="dct:source">https://github.com/eliranwong/OpenGNT</a>.



