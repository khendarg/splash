#!/usr/bin/env python2
from __future__ import print_function

import re
import nltk

from nltk.corpus import stopwords

def seek_substrate_words(text):
	substrate_words = ['transport', 'transports', 'transported', 'transporting', 'uptake', 'import', 'export', 'efflux', 'influx', 'porter']
	if type(text[0]) is unicode: substrate_words = [unicode(w) for w in substrate_words]
	for w in substrate_words: 
		if w in text: print(text.concordance(w))

def parse_text(x):
	x = re.sub('\([^)]*\)', '', x)
	raw = nltk.word_tokenize(x)
	lower = [c.lower() for c in raw]

	text = nltk.Text(lower)

	seek_substrate_words(text)
	#poss = nltk.pos_tag(text)

	#sw = stopwords.words('english')
	#verbs = []
	#for x in poss:
	#	if x[1][:2] == 'VB' and x[0] not in sw: 
	#		verbs.append(x[0])
	#		#print(str(x[0]),',', x[1])
	#for v in verbs: print(v)

def clean_html(x): 
	x = re.sub('<[^>]*>', '', x)
	x = re.sub('&[^;]*;', '', x)
	return x

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('infile', default='claudins.txt', nargs='+')
	parser.add_argument('-c', action='store_true', help='clean HTML')
	args = parser.parse_args()

	for fn in args.infile:
		f = open(fn)
		x = f.read()
		f.close()
		if args.c: x = clean_html(x)

		parse_text(x.decode('utf-8'))
