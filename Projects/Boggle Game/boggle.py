"""
File: boggle.py
Name:
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
moveset = [(0, 0), (-1, -1), (0, -1), (1, -1), (-1, 0),  (1, 0), (-1, 1), (0, 1), (1, 1)]
START_X = 0
START_Y = 0

def main():
	"""
	TODO:
	"""

	used_set = []
	word_making = ""
	count = 0
	found = []
	row1 = input("input row1: ")
	if len(row1) != 7:
		print("illegal format!")
		row1 = input("input row1: ")
	for letter in range(len(row1)):
		if letter % 2 !=0:
			if row1[letter] != " ":
				print("illegal format!")
				row1 = input("input row1: ")
	row2 = input("input row2: ")
	if len(row2) != 7:
		print("illegal format!")
		row1 = input("input row2: ")
	for letter in range(len(row2)):
		if letter % 2 != 0:
			if row1[letter] != " ":
				print("illegal format!")
				row1 = input("input row2: ")
	row3 = input("input row3: ")
	if len(row3) != 7:
		print("illegal format!")
		row1 = input("input row3: ")
	for letter in range(len(row3)):
		if letter % 2 != 0:
			if row1[letter] != " ":
				print("illegal format!")
				row1 = input("input row3: ")
	row4 = input("input row4: ")
	if len(row4) != 7:
		print("illegal format!")
		row1 = input("input row4: ")
	for letter in range(len(row3)):
		if letter % 2 != 0:
			if row1[letter] != " ":
				print("illegal format!")
				row1 = input("input row4: ")
	# row1 = "fy cl"
	# row2 = "iomg"
	# row3 = "oril"
	# row4 = "hjhu"
	grid = [row1.replace(" ", ""), row2.replace(" ", ""), row3.replace(" ", ""), row4.replace(" ", "")]
	for x in range(len(grid)):
		for y in range(len(grid)):
			find_words(x, y, used_set, grid, word_making, count, found)
	print(f"found {len(found)} words")



def read_dictionary(FILE):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	python_list = []
	with open(FILE, "r") as f:
		for line in f:
			line = line.strip()
			python_list.append(line)
	return python_list


d = read_dictionary(FILE)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	# """
	for word in d:
		if word.startswith(sub_s):
			return True
	return False
	# pass


# def find_words(x, y, used_set, grid, word_making, count):
# 	if word_making.lower() in d and len(word_making) >= 4:
# 		print(f"good: {word_making}")
# 		count += 1
# 	if has_prefix(word_making) is False:
# 		word_making = ""
# 		return word_making
# 	else:
# 		if (x, y) not in used_set and 0 <= x <= 3 and 0 <= y <= 3:
# 			word_making += grid[y][x]
# 			print(word_making)
# 			used_set.append((x, y))
# 			for dx, dy in moveset:
# 				nx, ny = x+dx, y+dy
# 				find_words(nx, ny, used_set, grid, word_making, count)


def find_words(x, y, used_set, grid, word_making, count, found):
	if word_making.lower() in d and len(word_making) >= 4 and word_making not in found:
		print(f"found: {word_making}")
		found.append(word_making)
	if len(word_making) > 1 and has_prefix(word_making) is False:
		return
	else:
		# if (x, y) not in used_set and 0 <= x <= 3 and 0 <= y <= 3:
			# word_making += grid[x][y]
			# print(word_making)
			# print(used_set)
		for dx, dy in moveset:
			nx, ny = x+dx, y+dy
			if (nx, ny) not in used_set and 0 <= nx <= 3 and 0 <= ny <= 3:
				word_making += grid[nx][ny]
				used_set.append((nx, ny))
				find_words(nx, ny, used_set, grid, word_making, count, found)
				used_set.remove((nx, ny))
				word_making = word_making[:-1]
	return found






	# if (x, y) not in used_set and 0 <= x <= 3 and 0 <= y <= 3:
	# 	word_making += grid[y][x]
	# 	print(word_making)
	# 	used_set.append((x, y))
	# 	for dx, dy in moveset:
	# 		nx, ny = x+dx, y+dy
	# 		find_words(nx, ny, used_set, grid, word_making, count)



if __name__ == '__main__':
	main()
