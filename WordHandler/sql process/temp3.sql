    create table temp3 as 
    SELECT temp2.word as temp2word, Z4.word as Z4word, freqcet4,freqcet6,freqz4 FROM temp2 LEFT JOIN z4 ON temp2.word=z4.word 
    UNION
    SELECT temp2.word as temp2word, Z4.word as Z4word, freqcet4,freqcet6,freqz4 FROM temp2 RIGHT JOIN z4 ON temp2.word=z4.word  ;