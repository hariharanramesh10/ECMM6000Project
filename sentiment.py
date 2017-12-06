import csv
from textblob import TextBlob

inputfile = raw_input("\nEnter the input filename\n")
outputfile = 'sentiment.csv'

with open (inputfile, 'r') as csvfile:
	columns = csv.reader(csvfile)
	with open (outputfile, 'wb') as outfile:
		writer = csv.writer(outfile)
		writer.writerow(["Tweet","Sentiment-Polarity","Sentiment-subjectivity"])
		for column in columns:
			sentence = column[3]
			blob = TextBlob (sentence)
			writer.writerow([sentence,blob.sentiment.polarity,blob.sentiment.subjectivity])
				