#!/usr/bin/env python

if __name__ == "__main__":
    with open("hamlet.txt","r") as f:
        wordcount={}
        for line in f.readlines():
            # remove special characters
            line = line.translate({ord(i):' ' for i in '!?@#$,.;:[]()'})
            # normalise words to lowercase
            line = line.lower()

            for word in line.split():
                if word not in wordcount:
                    wordcount[word] = 0
                wordcount[word] += 1

        # sort by count descending and takes top 5 elements
        top_words = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)[:10]

        for word, count in top_words:
            print(f"word: {word}, count: {count}")

