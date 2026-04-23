def len_of_text(text):
	if "\n" in text:
		texts = text.split("\n")
		max_len = len(texts[0])
		for elem in texts:
			if len(elem) > max_len:
				max_len = len(elem)
		return max_len
	
	else:
		return len(text)

def draw (text, ascci_file, offset):
	try :
		text = text.expandtabs(4)
		lenght = len_of_text(text)
		lines = text.split("\n")
		print (" "*offset + "/" + "^"*lenght + "\\")
		for line in lines:
			print (" "*(offset - 1) + "| " + line + " "*(lenght-len(line)) + " |")
		print (" "*offset + "\\" + "_"*lenght + "/")
		print (" "*offset +"/" + "\n" + " "*(offset - 1) + "/")
		with open (ascci_file, "r") as file :
			line_list = file.readlines ()
			for line in line_list :
				print (line , end ="")
			print("\n")
				
	except FileNotFoundError:
		print (f"{ascci_file} doesn't exist.\n")
	
	except TypeError:
		print (f"{ascci_file} given isn't string.\n")
		
	except PermissionError:
		print (f"permission denied (you can't access {ascci_file}).\n")
	
	except UnicodeDecodeError:
		print (f"{ascci_file} is in an unexpected encoding (not UTF-8 or ANSI).\n")
		
	except IsADirectoryError:
		print (f"{ascci_file} is a directory, not a file.\n")
