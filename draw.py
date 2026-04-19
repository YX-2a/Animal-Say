def draw (text, ascci_file) :
	try :
		print (" "*10 + "/" + "^"*(len(text)) + "\\")
		print (" "*9 + "| " + text + " |")
		print (" "*10 + "\\" + "_"*(len(text)) + "/")
		print (" "*10 +"/" + "\n" + " "*9 + "/")
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
