def draw (text, ascci_file) :
	try :
		print (" "*10 + "/" + "^"*(len(text)) + "\\")
		print (" "*11 + text)
		print (" "*10 + "\\" + "_"*(len(text)) + "/")
		print (" "*10 +"/" + "\n" + " "*9 + "/")
		with open (ascci_file, "r") as file :
			line_list = file.readlines ()
			for line in line_list :
				print (line , end ="")
			print("\n")
				
	except FileNotFoundError:
		print ("File Doesn't exist\n")
	
	except TypeError:
		print ("Text given isn't string\n")
		
	except PermissionError:
		print ("You aren't permited to read file or directory\n")
	
	except UnicodeDecodeError:
		print ("File isn't a text file\n")
		
	except IsADirectoryError:
		print ("The Specified file is a directory\n")
		
	except OSError:
		print ("Operating System Error\n")