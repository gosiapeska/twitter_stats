import sys
import urllib
import json
import operator
import re

def happiest_state(tweets, dictionary):
	hashes = {}
	total = []
	
	for tweet in tweets:
		sentiment = 0
		row = json.loads(tweet)	
		if 'text' in row and 'user' in row:	
			address = row['user']['location']
			words = re.findall('[A-Z][A-Z]', address)
			texts = row['text'].split()			
			for word in texts:
				if word in dictionary:
					sentiment += float(dictionary[word])
			for word in words:
				if word != "UK":
					if word in hashes:
						hashes[word] += sentiment
					else:
						hashes[word] = sentiment 

	sorted_x = sorted(hashes.iteritems(), key=operator.itemgetter(1), reverse=True)		
	print sorted_x[0][0]

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
    happiest_state(tweet_file, dictionary)
    tweet_file.close()
    sent_file.close()

if __name__ == '__main__':
    main()