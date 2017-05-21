import sys
import urllib
import json
import re

def calculate_sentiment(tweets, dictionary):
	thash = {}
	for tweet in tweets:
		row = json.loads(tweet)
		sentiment = 0
		if 'text' in row:
			words = row['text'].split()			
			for word in words:
				if word in dictionary:
					sentiment += float(dictionary[word])
			for word in words:
				if not word in dictionary:
					if word in thash:							
						thash[word] += sentiment
					else:
						thash[word] = sentiment
		print word.encode("utf-8"), sentiment
	for t in thash:
		print t, float(thash[t])
			
def get_dictionary(afinn):
	afinn_dict = {}
	affin_hash = []
	for line in afinn:
		affin_hash = line.split()
		string = " ".join(affin_hash[0:len(affin_hash)-1])
		afinn_dict[string] = float(affin_hash[-1]) 		
	return afinn_dict	

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2], "rw")
    dictionary = get_dictionary(sent_file)
    calculate_sentiment(tweet_file, dictionary)
    tweet_file.close()
    sent_file.close()

if __name__ == '__main__':
    main()
