import sys
import urllib
import json
import operator

def top_ten(tweets):
	hashes = {}
	total = []
	for tweet in tweets:
		row = json.loads(tweet)		
		if 'entities' in row:
			tags = row['entities']['hashtags']
			for tag in tags:				
				if tag['text'] in hashes:
					hashes[tag['text']] += 1
				else:
					hashes[tag['text']] = 1 

	sorted_x = sorted(hashes.iteritems(), key=operator.itemgetter(1), reverse=True)		
	for x in sorted_x[:10]:
		print x[0], x[1]
				

def main():
    tweet_file = open(sys.argv[1])
    top_ten(tweet_file)
    tweet_file.close()

if __name__ == '__main__':
    main()