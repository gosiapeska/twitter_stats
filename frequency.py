import sys
import urllib
import json

def calculate_frequency(tweets):
	frequencies = {}
	total = 0
	for tweet in tweets:
		row = json.loads(tweet)		
		if 'text' in row:
			words = row['text'].split()		
			for word in words:
				total += 1
				if word in frequencies:
					frequencies[word] += 1
				else:
					frequencies[word.encode("utf-8")] = 1
	for frequency in frequencies:
		print frequency, float(frequencies[frequency]) / total

def main():
    tweet_file = open(sys.argv[1])
    calculate_frequency(tweet_file)
    tweet_file.close()

if __name__ == '__main__':
    main()
