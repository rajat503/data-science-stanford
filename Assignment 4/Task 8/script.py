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
		print(s[2]+"	float	none	"+s[1]+'	no answers	false')
		j += 1
	i+= 1
		
