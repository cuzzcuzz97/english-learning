try:
	import sys
	import random
	from urllib.request import urlopen
	import os
	# tts
	import sys
	from googletrans import Translator, constants
	from pprint import pprint
except:
	os.system('pip install -r requirements.txt')
	

translator = Translator() # class





all_ans_words = []
all_wrong_words = []
def main():

	os.system('python get_dir.py')
	list_vocab = []

	with open('words_list.txt', 'r') as file:
		n = file.readlines()
		for w in n:
			w = w.replace('\n','')
			list_vocab.append(w)
	try:
		sys.argv[1]
		list_vocab.append(sys.argv[1])
	except:
		pass
	for i in range(len(list_vocab)):
		n = list_vocab[i].split('.')
		print(f'{i+1}. {n[0]}')
	# try:
	answer_part(int(input('Choose group of vocabulary you want to learn : ').strip()),list_vocab)
	# except:
	# 	sys.exit('Invalid select')

def generate_word(v):
	with open(v) as file:
		new = file.readlines()
	r_word = random.choice(new).replace('\n','')
	return r_word


def answer_part(n,list_vocab):
	point = 0
	while True:
		w = generate_word(f"words_file/{list_vocab[n-1]}")
		if len(w) > 2:
			q = hidden_part(w)
			print(q)
			ans = input("Enter word: ").strip().lower()
			if ans == 'stop':
				print('correct words:',all_ans_words)
				print('Incorrect words:',all_wrong_words)
				sys.exit('thank you')
			elif ans == 'translate':
				...
			if ans == w:
				point += 1
				print('Great job!')
				all_ans_words.append(ans)
				translate(w)
			else:
				print(w)
				all_wrong_words.append(w)
				print('Try again!')
				translate(w)

def translate(w):
	translation = translator.translate(w, dest="vi",src="en")
	# translation2 = translator.translate(w, dest="fr",src="en")
	print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

		

def hidden_part(word):
	word = word.upper()
	d = []
	for letter in word:
		d.append(letter)

	for i in range(len(d)//3):
		pos = random.randint(0,len(d))
		d[pos-1] = "_"
	question = ''.join(d)

	return question




if __name__ == "__main__":
	main()

