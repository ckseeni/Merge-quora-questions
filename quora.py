import pandas as p
dataset = p.read_csv("train.csv")
question1 = dataset['question1']
question2 = dataset['question2']
words = []
for x in question1:
    for i in x.split():
        words.append(i)
for x in question2:
    for i in x.split():
        words.append(i)
myset = set(words)
unique_words = list(myset)
matrix = [[0 for i in range(len(question1)*2)] for i in range(len(unique_words))]
for i in range(0,len(unique_words)):
    k=0
    for j in range(0,len(question1)):
        ques = question1[j].split()
        if unique_words[i] in ques:
            matrix[i][k] = 1
        k = k+1
    for j in range(0,len(question2)):
        ques = question2[j].split()
        if unique_words[i] in ques:
            matrix[i][k] = 1
        k = k+1
#for i in matrix:
#	print(i)
band_size = 3
hashed_matrix = [[0 for i in range(len(question1)*2)] for i in range(int(len(unique_words)/band_size))]
i=0
while i<len(unique_words)-(band_size-1):
    k=0
    elements = ""
    for j in range(0,len(question1)):
        for l in range(0,band_size):
            elements = elements + str(matrix[i+l][k])
        hashed_matrix[int(i/band_size)][k] = int(elements,2)  
        elements = ""
        k = k+1
    for j in range(0,len(question2)):
        for l in range(0,band_size):
            elements = elements + str(matrix[i+l][k])
        hashed_matrix[int(i/band_size)][k] = int(elements,2)  
        elements = "" 
        k = k+1
    i = i+band_size

hash_map = {}
for l in range(0,len(hashed_matrix)):
    k=0
    for m in range(0,len(question1)):
        if hashed_matrix[l][k]!=0:
            key = ""+str(hashed_matrix[l][k])+"-"+str(l)
            if key in hash_map:
                value = "Q1-"+str(m)
                bucket = hash_map[key]
                bucket.append(value)
                hash_map[key] = bucket
            else:
                value = "Q1-"+str(m)
                bucket = []
                bucket.append(value)
                hash_map[key] = bucket
        k = k+1
    for m in range(0,len(question2)):
        if hashed_matrix[l][k]!=0:
            key = ""+str(hashed_matrix[l][k])+"-"+str(l)
            if key in hash_map:
                value = "Q2-"+str(m)
                bucket = hash_map[key]
                bucket.append(value)
                hash_map[key] = bucket
            else:
                value = "Q2-"+str(m)
                bucket = []
                bucket.append(value)
                hash_map[key] = bucket
        k = k+1

#print(hash_map)
common_questions = []
for x in hash_map:
    q1=[]
    q2=[]
    l=[]
    l = hash_map[x]
    for i in l:
        if 'Q1' in i:
            newstr = int(i[3:])
            q1.append(newstr)
        if 'Q2' in i:
            newstr = int(i[3:])
            q2.append(newstr)
    if q1 and q2:
        common = list(set(q1).intersection(q2))
        common_questions.extend(common)
""" 
myset = set(common_questions)
common_questions = list(myset)
common_questions.sort()
print(common_questions)"""
#print(common_questions)
h = {}
for i in common_questions:
	if i in h:
		c = h[i]
		c = c + 1
		h[i] = c
	else:
		h[i] = 1
print(h)
for i in h:
	ques1 = question1[i]
	ques2 = question2[i]
	q1 = ques1.split()
	q2 = ques2.split()
	l1 = len(q1)
	l2 = len(q2)
	t = 0
	if l1>l2:
		t = int(l1/3)	
	else:
		t = int(l2/3)
	if h[i]>=t:
		print(i)

#remove most frequent words and result questions will be taken only if it is repeated in large number of times


