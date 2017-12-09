*****************Natural Language Processing Project***************
********* Text Summarization ***************

Prerequisites:

1. Python 3.5
2. Latest nltk
3. Latest nltk_data
4. textblob installation
5. pprint
6. numpy

The program has been tested in the above environment on Windows and works fine.

1. Run the program as:

>python textsummarization.py "Data\Data.txt"

2. For examples and help usage:

>python textsummarization.py -h

3. The list of stopwords used is:
Link: https://gist.github.com/sebleier/554280

a. The file Wordlist has been kept in a way that all stopwords are on newline.
b. Any new stopwords list should comply with such format for the program to be successful
c. The file Wordlist should be in the same directory as lesk.py

4. The list for positive words,negative words,incrementer words and decrementer words should be in the dicts folder
positive.yml
negative.yml
inc.yml
inv.yml
Any new lists should comply with such format for the program to be successful
