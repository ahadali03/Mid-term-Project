from textblob import TextBlob
import nltk


def get_nouns_tagcount (textstring):
    ''' When there is a textstring, textblob will analyze it to find the amount of tags and noun phrases within '''
    blob = TextBlob (textstring)
    tagcount = len (blob.tags)
    #Counts tags
    p = blob.noun_phrases
    #Gets noun phrases
    return tagcount, p
text1 = "I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail cells. And some of you have come from areas where your quest -- quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that unearned suffering is redemptive. Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our northern cities, knowing that somehow this situation can and will be changed."
text2 = "And you and I are in a double trap because not only do we lose by taking our money someplace else and spending it, when we try and spend it in our own community we're trapped because we haven't had sense enough to set up stores and control the businesses of our community. The man who is controlling the stores in our community is a man who doesn't look like we do. He's a man who doesn't even live in the community. So you and I, even when we try and spend our money on the block where we live or the area where we live, we're spending it with a man who, when the sun goes down, takes that basket full of money in another part of the town."
tags1, np1 = get_nouns_tagcount(text1)
print ("Martin Luther King's speech has {} tags and the nouns are:\n{}".format (tags1, np1))
tags2, np2 = get_nouns_tagcount(text2)
print ("Malcolm X's speech has {} tags and the nouns are:\n{}".format (tags2, np2))
#The nouns are printed out to help easily identify how many exist in each speech
if (tags1 > tags2):
    print ("There are more tags in Dr. King's speech")
else:
    print ("There are more tags in Malcolm X's speech")
if (len (np1) > len (np2)):
    print ("There are more nouns in Dr. King's speech")
else:
    print ("There are more nouns in Malcolm X's speech")