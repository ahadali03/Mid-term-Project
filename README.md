# Mid-term-Project

# Package Summary
The package is able to analyze any form of written texts, for example newspaper excerpts, quotes from books, or even written down speeches, once there is a form of text to analyze, the code is able to determine how many nouns as well as tags (conjunctions, adjectives, numerals...). It can take two or more text excerpts and compare them to see which one has more nouns and which one has more tags. However, the cool thing about this code is that one can choose which tag to be targeted, for example if one wants to find out the amount of adjectives instead of nouns, they can us this code 
def get_adjectives(text):
    blob = TextBlob(text)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]

df['adjectives'] = df['reviews'].apply(get_adjectives)
There are many more possiblities regarding parts of speech with this code which is why it can be so useful in an English or grammar based class

# Install and Run Instructions
Step 1:
Install TextBlob

$ pip install -U textblob
$ python -m textblob.download_corpora

Step 2 - Install nltk
run pip install --user -U nltk

Step 3 - Install nltk data
import nltk
nltk.download()
!!! If issues occur and steps to install nltk data do not work this method can also be used to help !!!
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
