import sys

numbers=[6,20,33,35,58,73,77,84,94,113,114,123,143,175,176,247,398,426,435,470]
print('correct_answer	answer_type	asset_type	asset_file	possible_answers	randomize_answers')
f = open('CollectionData.csv', 'r')
i=1
j=0
for line in f:
	if j==20 :
		break
	if i==numbers[j] :
		s = line.split('","')
		s[2]=s[2].replace('$','').replace('"','').strip('\n\r')
		j += 1
		k=''.join(e for e in s[1] if e.isalnum() or e==' ')
		k=k.lower()
		k=k.replace(' ','_')
		k=k.replace('__','_')
		k=k+".txt"
		print(s[2]+"	float	text	"+k+'	no answers	false')
		w=open("assets/"+k, 'w')
		w.write(s[1])
		w.close()
	i+= 1
		
