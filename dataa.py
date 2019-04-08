# -*- coding: utf-8 -*-
import statistics

# Parses the tweet text for analysis.
def parsi(name):
    file = open(name +"_tweets.csv", "r", encoding="utf-8")
    f = open(name+"_dump.txt", "a")
    for line in file:
        if line != None:
            text = line.split(",")
            if len(text) > 2:
                f.write(text[3] + ";")

    f.close()
    statistics.stats(name)

