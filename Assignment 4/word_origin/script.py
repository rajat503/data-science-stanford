import sys

print('correct_answer	answer_type	asset_type	asset_file	possible_answers	randomize_answers')
f = open('tasks.tsv', 'r')
for line in f:
	s = line.split('\t')
	k=s[3].lower()
	k=k.replace(' ','_')
	k=k+".txt"
	w=open("assets/"+k, 'w')
	w.write(s[3])
	w.close()
		