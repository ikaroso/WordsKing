    create table temptest as 
    SELECT cet4.word as cet4word, cet6.word as cet6word, freqcet4,freqcet6 FROM cet4 LEFT JOIN cet6 ON cet4.word=cet6.word 
    UNION
    SELECT cet4.word as cet4word, cet6.word as cet6word, freqcet4,freqcet6 FROM cet4 RIGHT JOIN cet6 ON cet4.word=cet6.word ;