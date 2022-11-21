#!/usr/bin/python3

#sentence1 = "the quick", sentence2 = "brown fox", 
#return ["the", "quick", "brown", "fox"]
#sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", 
#return ["beat", "to", "lost"]
#sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", 
#return ["copper", "hot"]

sentence1 = "the tottoise beat the haire"
sentence2 = "the tortoise lost to the haire"

def notInSentence(sentence1, sentence2):
	newlist = []
	S1 = sentence1.split()#splits the sentence into a list using the spaces
	S2 = sentence2.split()

	for i in S2:
		if i not in S1:
			newlist.append(i)
	for i in S1:
		if i not in S2:
			newlist.append(i)
			return newlist

print(notInSentence(sentence1, sentence2))
