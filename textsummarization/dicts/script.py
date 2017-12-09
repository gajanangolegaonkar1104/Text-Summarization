import sys

with open('negativewords.txt') as f:
	words = [word.strip() for word in f]

with open('newnegativewords.txt','w') as f1:
	for word in words:
		f1.write(word+":"+" "+"[negative]")
		f1.write("\n")
