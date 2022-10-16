from urllib.request import urlopen


with open('new_10000_words.txt', 'w') as file:
	word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
	response = urlopen(word_site)
	txt = response.read().decode()
	for w in txt:
		w = w.replace('<br>','')
		file.write(w)
		# print(txt)
		# x = x.replace('<p>','')
		# x = x.replace('</p>','')
		# file.write(x)
		# file.write(x)








# from urllib.request import urlopen


# word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
# response = urlopen(word_site)
# txt = response.read().decode()
