from sys import argv, exit
from os import path, name as os_name
from draw import draw

string = ""
animal = ""
escape = False
offset = 10

default_dir = ""
if os_name == "nt":
	default_dir = path.expandvars("%APPDATA%\\animsay\\")
	if not path.exists(default_dir):
		default_dir = path.expanduser("%PROGRAMDATA%\\animsay\\")
		if not path.exists(default_dir):
			default_dir = "./"

elif os_name == "posix":
	default_dir = path.expanduser("~/.config/animsay/")
	if not path.exists(default_dir):
		default_dir = "/etc/animsay/"
		if not path.exists(default_dir):
			default_dir = "./"


def_dir = default_dir + "animals"

help_text = f"usage: {path.basename(argv[0])} [options] animal \"string\"\noptions:\n\t-d, --directory DIR\tDirectory of the animals (Default is {def_dir})\n\t-h, --help\t\tDisplay This Text\n\t-e, --escape\t\tAllow escape sequences (\\n, \\t etc...)\n\t-o, --offset NUM\tOffset the text bubble by NUM (Default is {offset})"

if len(argv) <= 1:
	print("Not Enough Arguments")
	exit()

if argv[1] == "-h" or argv[1] == "--help":
	print(help_text)
	exit()

if "-e" in argv or "--escape" in argv:
	escape = True
	if "-e" in argv:
		argv.pop(argv.index("-e"))
	
	elif "--escape" in argv:
		argv.pop(argv.index("--escape"))

if "-o" in argv or "--offset" in argv:
	if "-o" in argv:
		offset = int(argv[argv.index("-o") + 1])
		argv.pop(argv.index("-o") + 1)
		argv.pop(argv.index("-o"))

	elif "--offset" in argv:
		offset = int(argv[argv.index("--offset") + 1])
		argv.pop(argv.index("--offset") + 1)
		argv.pop(argv.index("--offset"))

if argv[1] == "-d" or argv[1] == "--directory":
	if len(argv) <= 4:
		print("Not Enough Arguments")
		exit()

	def_dir = argv[2]
	argv.pop(1)
	argv.pop(1)

animal = argv[1]
string = argv[2]

if escape:
	result_string = ""
	sequence = ""
	for char in string:
		if char == "\\":
			sequence += char
		else:
			if sequence:
				if len(sequence) == 1:
					result_string += (sequence[0] + char).encode().decode("unicode_escape")
				
				elif len(sequence) % 2 == 0:
					result_string += sequence[:len(sequence)//2]
					result_string += char
				
				else:
					seq = sequence[:-1]
					result_string += seq[:len(seq)//2 ]
					result_string += (sequence[-1] + char).encode().decode("unicode_escape")
				sequence = ""
			
			else:
				result_string += char
	string = result_string

sep = ""

if def_dir[-1] != "/":
	sep = "/"

elif def_dir[-1] != "\\":
	sep = "\\"

draw (string, def_dir + sep + animal + ".txt", offset)