input_text = open('input.txt', 'r').read()

input_list = input_text.split("\n")

def part_one():
	count_valid_passphrases = 0
	for item in input_list:
		words = item.split(" ")
		seen = set()
		duplicate = False
		for word in words:
			if word in seen:
				duplicate = True
				break
			seen.add(word)
		if duplicate == False:
			count_valid_passphrases+=1
	print(count_valid_passphrases)

def part_two():
	count_valid_passphrases = 0
	for item in input_list:
		words = item.split(" ")
		seen = set()
		duplicate = False
		for word in words:
			word_in_order = ''.join(sorted(word))
			if word_in_order in seen:
				duplicate = True
				break
			seen.add(word_in_order)
		if duplicate == False:
			count_valid_passphrases+=1
	print(count_valid_passphrases)



part_two()
