f = open("name.py", "r")
file_content = f.read().__str__()

num_lines = file_content.count("\n")
words = file_content.count(" ") 
letters = file_content.count("")

print("Words: {}\nLines: {}\nWords: {}".format(words, num_lines, letters))
