import numpy as np
import nltk
#nltk.download("punkt")
sad=[]
happy=[]
for line in open('sad.txt'):
    sad.append(nltk.word_tokenize(line.lower()))
for line in open('happy.txt'):
    happy.append(nltk.word_tokenize(line.lower()))
#print(sad)

dict=set()
for tweet in sad:
    for word in tweet:
        dict.add(word)
for tweet in happy:
    for word in tweet:
        dict.add(word)

#Calculate Phi
phi=(len(happy)+1)/(len(happy)+len(sad)+2)
#print(phi)
#Calculate PhiIs for each word knowing sad
phiSad={}
for dictword in dict:
    phiSad[dictword]=1
    for tweet in sad:
        for word in tweet:
            if(dictword == word ):
                phiSad[dictword]+=1
                break

for k in phiSad:
    phiSad[k]=phiSad[k]/(len(sad)+2)
#calculate PhiIs for each word knowing happy
phiHappy={}
for dictword in dict:
    phiHappy[dictword]=1
    for tweet in happy:
        for word in tweet:
            if(dictword == word ):
                phiHappy[dictword]+=1
                break
for k in phiHappy:
    phiHappy[k]=phiHappy[k]/(len(happy)+2)

#Predict
phrase=""
while(phrase!="/"):
    phrase =input("Enter a phrase : ")
    #tokenize
    words=nltk.word_tokenize(phrase.lower())
    #Fit to sad and happy models
    #P(x|sad)
    probGivenSad=1
    #P(x|happy)
    probGivenHappy=1
    for word in words:
        if word in phiSad and word in phiHappy:
            probGivenSad*=phiSad[word]
            probGivenHappy*=phiHappy[word]
    #Denominator P(x)
    pOfX=probGivenSad*(1-phi)+probGivenHappy*phi
    #P(sad|x)
    finalProbabilitySad=probGivenSad*(1-phi)/pOfX
    #P(happy|x)
    finalProbabilityHappy=probGivenHappy*phi/pOfX
    print("Proba Sad : ")
    print(finalProbabilitySad)
    print("Proba Happy : ")
    print(finalProbabilityHappy)
    #greatest prob => prediction
    if finalProbabilityHappy>finalProbabilitySad:
        print("Happy Phrase")
    else:
        print("Sad Phrase")
    resp=int(input("Was it a sad (0) or happy (1) phrase ? "))
    if resp==0:
        with open("sad.txt", "a") as f:
            f.write('\n'+phrase)
    else:
        with open("happy.txt", "a") as f:
            f.write('\n'+phrase)
    	# Anything you want to do with the file
