# OGNTa (OpenGNT Abridged)

This is an abridged and updated version of OpenGNT Version 3 [OGNT 3.3 Base Text](https://github.com/eliranwong/OpenGNT/blob/master/OpenGNT_BASE_TEXT.zip)

## Structure changes

-  OGNT3.3 abridged to the following tab-separated columns:
   -  OGNTsort = sort numbers of all words of the base text of OGNT.
   -  Book-Chapter:Verse = scripture reference.
   -  PMpWord-OGNT-PMfWord = OGNT and punctuation marks.
      - PMpWord = punctuation mark(s) preceding the main word.
        - [[ changed to ⟦
        - ]] changed to ⟧
      - OGNT = Greek word of OGNT in accented form.
      - PMfWord = punctuation mark(s) following the main word.
   -  lexeme = Greek word of OGNT in lexical form.
   -  rmac = Robinson's Morphological Analysis Codes.
   -  TBESG = context-insensitive glosses (from Tyndale House's TAGNT).
   -  IT = context-sensitive glossess (from Berean Interlinear Bible)

| OGNTsort | Book-Chapter:Verse | PMpWord OGNTa PMfWord | lexeme               | rmac    | TBESG        | IT                 |
|----------|--------------------|-----------------------|----------------------|---------|--------------|--------------------|
| 000001   | 40-1:1             | Βίβλος                | βίβλος               | N-NSF   | book         | [The] book         |
| 000002   | 40-1:1             | γενέσεως              | γένεσις              | N-GSF   | origin       | of [the] genealogy |
| 000003   | 40-1:1             | Ἰησοῦ                 | Ἰησοῦς               | N-GSM-P | Jesus/Joshua | of Jesus           |
| 000004   | 40-1:1             | Χριστοῦ               | Χριστός              | N-GSM-T | Christ       | Christ,            |
| 000005   | 40-1:1             | υἱοῦ                  | υἱός                 | N-GSM   | son          | son                |
| 000006   | 40-1:1             | Δαυὶδ                 | Δαυείδ, Δαυίδ, Δαβίδ | N-GSM-P | David        | of David,          |
| 000007   | 40-1:1             | υἱοῦ                  | υἱός                 | N-GSM   | son          | son                |
| 000008   | 40-1:1             | Ἀβραάμ . ¶            | Ἀβραάμ               | N-GSM-P | Abraham      | of Abraham:        |



## Content changes
- `018408	41-1:5	Ἰουδαία	N-NSF-L` ⇒ `A-NSF-L`
- `044656	42-19:21	αὐστηρὸς	P-NSM` ⇒ `A-NSM`
- `044681	42-19:22	αὐστηρός	P-NSM` ⇒ `A-NSM`
- 

---

## License :

The entire text of OGNTa is released under the following license:


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">OGNTa is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

---

## Attribution :

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Open Greek New Testament Project</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://marvel.bible" property="cc:attributionName" rel="cc:attributionURL">Eliran Wong</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="https://github.com/eliranwong/OpenGNT" rel="dct:source">https://github.com/eliranwong/OpenGNT</a>.



