import random
random.seed(10)

# Generate corpus of sentences for replicating Elman's SRN experiment with simple sentences
num_sentences = 10000

N_HUM = ['man', 'woman', 'boy', 'girl']
N_AGRESS = ['dragon', 'monster', 'lion']
N_ANIM = N_HUM + N_AGRESS + ['cat', 'mouse', 'dog']
N_FRAG = ['glass', 'plate']
N_FOOD = ['cookie', 'bread', 'sandwich']
N_INANIM = N_FRAG + N_FOOD + ['book', 'rock', 'car']
V_INTRAN = ['think', 'sleep', 'exist']
V_TRAN = ['see', 'chase', 'like']
V_AGPAT = ['move', 'break']
V_PERCEPT = ['smell', 'see']
V_DESTROY = ['break', 'smash']
V_EAT = ['eat']

templates = []
templates.append([N_HUM, V_EAT, N_FOOD])
templates.append([N_HUM, V_PERCEPT, N_INANIM])
templates.append([N_HUM, V_DESTROY, N_FRAG])
templates.append([N_HUM, V_INTRAN])
templates.append([N_HUM, V_TRAN, N_HUM])
templates.append([N_HUM, V_AGPAT, N_INANIM])
templates.append([N_HUM, V_AGPAT])
templates.append([N_ANIM, V_EAT, N_FOOD])
templates.append([N_ANIM, V_TRAN, N_ANIM])
templates.append([N_ANIM, V_AGPAT, N_INANIM])
templates.append([N_ANIM, V_AGPAT])
templates.append([N_INANIM, V_AGPAT])
templates.append([N_AGRESS, V_DESTROY, N_FRAG])
templates.append([N_AGRESS, V_EAT, N_HUM])
templates.append([N_AGRESS, V_EAT, N_ANIM])
templates.append([N_AGRESS, V_EAT, N_FOOD])

vocab = set(sum(sum(templates,[]),[]))
print('vocab size',len(vocab))

with open('elman_sentences.txt','w') as fid:
	for i in range(num_sentences):
		T = random.choice(templates)
		S = []
		for mylist in T:
			S.append(random.choice(mylist))
		fid.write(' '.join(S) + '\n')