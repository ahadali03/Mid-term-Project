# Mid-term-Project

# Package Summary
The package is able to analyze any form of written texts, for example newspaper excerpts, quotes from books, or even written down speeches, once there is a form of text to analyze, the code is able to determine how many nouns as well as tags (conjunctions, adjectives, numerals...). It can take two or more text excerpts and compare them to see which one has more nouns and which one has more tags. However, the cool thing about this code is that one can choose which tag to be targeted, for example if one wants to find out the amount of adjectives instead of nouns, they can us this code 
def get_adjectives(text):
    blob = TextBlob(text)
    return [ word for (word,tag) in blob.tags if tag == "JJ"]

df['adjectives'] = df['reviews'].apply(get_adjectives)
There are many more possiblities regarding parts of speech with this code which is why it can be so useful in an English or grammar based class

# Install and Run Instructions
!!! open and run the file TextBlob.py !!!
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
# Code
For this code to function correctly, there are many key lines of code that must be included
For example, in line 5 the get_nouns_tagcount command is what is able to analyze the text and pull out all the nouns from it and number how many exist
This only gives us the number of nouns, so to find out what the nouns are, in line 17 and 18, it pulls out all the nouns from whatever text is in place which is very useful as you can quickly and easily access the nouns.
# Future Idea
This code can be very useful in a classroom environment for students who want to analyze a large text to quickly find out information about it. This can save a lot of time and the comparison feature can also help as it can determine which texts have more parts of speech. Although it is quite simple, if worked on further the code can advance to an even higher level and perhaps accomplish more tasks. Overall, it is a simple yet efficient code that many people can use to help in any type of learning based environment that involves grammar and syntax.
