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
				
	except FileNotFoundError:
		print ("File Doesn't exist")
	
	except TypeError:
		print ("Text given isn't string")
		
	except PermissionError:
		print ("You aren't permited to read file or directory")
	
	except UnicodeDecodeError:
		print ("File isn't a text file")
		
	except IsADirectoryError:
		print ("The Specified file is a directory")
		
	except OSError:
		print ("Operating System Error")