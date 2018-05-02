import pandas as pd
import math
from math import log
import re
from collections import Counter
import time
import re

df = pd.read_csv("dataminer (6).csv")

CT = df["Tweet"]

# for n in range(1, len(CT)-1):
# 		CT[n] = (re.split("[^a-zA-Z]*", CT[n]))

# print CT[0]

# type(CT[0])
# for w in re.split("[^a-zA-Z]*", CT[0]):
# 	print w

RT = df["Tweet"].sample(n = int(math.ceil((len(df)*0.3))))

#CK = ["brutal", "brutally", "murder", "rape", "kindnap", "kidnapping", "death", "penalty", "Zainab", "hang", "sexual", "abuse", "violence", "harass", "harassment", "harasser", "harassers", "honor", "honour", "killing", "child", "children", "women"]

CK = ["Zainab", "sexual", "abuse", "violence", "harass", "harassment", "harasser", "harassers", "honor", "killing", "honour", "killing", "child","children","women"]

UW = ["terrorism", "militant", "pashtun", "pashtoon", "anniversary", "bombing", "Hazara", "Hazaras", "Israel", "Palestine", "Syria", "Bhutto", "terrorist"]

# print len(RT)
# print len(CT)

def calEntropy(CT,w, freq_w):
	entropy = float(0)
	len_CT = float(len(CT))
	lbd = float(1)
	for tweet in CT:
		freq = tweet.count(w)
		val = float((freq + lbd)/(freq_w + len_CT * lbd))
		entropy = entropy - (val * log(val, 2))
	return entropy

V_CT = []
for ct in CT:
	ct = re.sub(r"http\S+", "", ct)
	for w in re.split("[^a-zA-Z]*", ct):
		V_CT.append(w)

V_RT = []
for rt in RT:
	rt = re.sub(r"http\S+", "", rt)
	for w in re.split("[^a-zA-Z]*", rt):
		V_RT.append(w)
freq_CT = Counter(V_CT)
freq_RT = Counter(V_RT)


def InitialRanking(CT, RT, CK, UW, V_CT, V_RT, freq_RT, freq_CT):
	WE = []

	#minFreq = int(math.ceil((len(V_CT) * 0.3)))
	minFreq = 5
	done_w = []
	for w in V_CT:
		if (w not in CK) and (w not in UW):
		# time.sleep(1)
			if (freq_RT[w] + freq_CT[w]) > minFreq:
				if freq_CT > freq_RT:
					if w not in done_w:
						e_w = calEntropy(CT,w, freq_CT[w])
						WE.append([w,e_w])
						done_w.append(w)
	return WE
	# for w in V:
	# 	if (w not in CK) and (w not in UW):

def findTweets(SK, w, CT):
	tweetSet = []
	for tweet in CT:
		tweet = re.sub(r"http\S+", "", tweet)
		if w in tweet:
			tweetSet.append(tweet)
	return tweetSet

def intersection(t, CK):
	for w in re.split("[^a-zA-Z]*", t):
		if w in CK:			
			return 1
	return 0

def ReRanking(SK, CK, CT, V_CT):
	WR = []
	for w in SK:
		T_w = findTweets(SK, w, CT)
		H_w = 0
		for t in T_w:
			if intersection(t, CK) != 0:
				H_w = H_w + 1
		r_w = (float(H_w)/float(len(T_w)))
		WR.append([w,r_w])
	WR.sort(key = takeSecond)
	WR_words = []
	for elem in WR:
		WR_words.append(elem[0])
	return WR_words
def takeSecond(elem):
    return elem[1]

def RankAndSelect(WE, N):
	WE.sort(key = takeSecond)
	n = 0
	top_N = []
	for elem in WE:
		if n < N:
			top_N.append(elem[0])
			n = n + 1
		else:
			break
	return top_N

# SK = RankAndSelect(InitialRanking(CT, RT, CK, UW, V_CT, V_RT, freq_RT, freq_CT),20)

# NR = ReRanking(SK, CK, CT, V_CT)

inputted = ""

while inputted != "stop":
	inputted = ""
	indexes = []
	SK = RankAndSelect(InitialRanking(CT, RT, CK, UW, V_CT, V_RT, freq_RT, freq_CT),10)
	NR = ReRanking(SK, CK, CT, V_CT)
	print "NR: ",NR
	for x in range(0,(len(NR)-1)):
		print x,": ",NR[x]
	print "Which of these do you want included in CK? Type no more to stop"
	while inputted != "no more":
		inputted = raw_input("Index: ")
		if inputted == "stop":
			break
		if inputted == "no more":
			break
		indexes.append(int(inputted))
		CK.append(NR[int(inputted)])
	for x in range(0, len(NR)-1):
		if x not in indexes:
			UW.append(NR[x])

print CK