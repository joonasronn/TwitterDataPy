# -*- coding: utf-8 -*-
import collections
import pandas as pd
import matplotlib.pyplot as plt


# Read input file, note the encoding is specified here 
# It may be different in your text file
def stats(name):
    file = open(name+"_dump.txt", encoding="utf-8")
    a= file.read()
    # Stopwords // you'll need to create one for yourself. These typically contain words like "and" "no" "rt" etc, supplied one is in finnish
    stopwords = set(line.strip() for line in open('stopwords.txt'))
    stopwords = stopwords.union(set(['RT','HTTPS']))
    # Instantiate a dictionary, and for every word in the file, 
    # Add to the dictionary if it doesn't exist. If it does, increase the count.
    wordcount = {}
    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("\\n","")
        word = word.replace(";b'","")
        word = word.replace("'","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        #This line is for fixing nordic characters
        word = word.replace("\\xc3\\xa4","ä").replace("\\xc3\\xb6","ö").replace("\\xc3\\xa5","å")
        if word not in stopwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    # Print most common word
    n_print = int(input("How many most common words to print: "))
    print("\nOK. The {} most common words are as follows\n".format(n_print))
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        print(word, ": ", count)
    # Close the file
    file.close()
    # Create a data frame of the most common words 
    # Draw a bar chart
    lst = word_counter.most_common(n_print)
    df = pd.DataFrame(lst, columns = ['Word', 'Count'])
    df.plot.bar(x='Word',y='Count')