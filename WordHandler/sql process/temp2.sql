create table temp2
select cet4word as word,freqcet4,freqcet6 from temptest where cet6word is null
	union
select cet6word as word,freqcet4,freqcet6 from temptest where cet4word is null
	union
select cet4word as word,freqcet4,freqcet6 from temptest where cet6word =cet4word
	;