#!/usr/bin/env python
with open("hamlet.txt","r") as f: 
    wordcount={} 
    for word in f.read().split(): 
        if word not in wordcount: 
            wordcount[word] = 0
        wordcount[word] += 1
    print([(word, count) for word, count in wordcount.items()])