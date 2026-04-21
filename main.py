from sys import argv
from draw import draw

string = ""
animal = ""
escape = False
def_dir = "./animals"
help_text = f"usage: {argv[0]} [options] animal \"string\"\noptions:\n\t-d, --directory DIR\tDirectory of the animals (Default is {def_dir})\n\t-h, --help\t\tDisplay This Text\n\t-e, --escape\t\tAllow escape sequences (\\n, \\t etc...)\n"

if len(argv) <= 1:
	print("Not Enough Arguments")
	exit()

if argv[1] == "-h" or argv[1] == "--help":
	print(help_text)

if "-e" in argv or "--encoding" in argv:
	escape = True
	if "-e" in argv:
		argv.pop(argv.index("-e"))
	
	elif "--encoding" in argv:
		argv.pop(argv.index("--encoding"))

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
	string = string.replace("\\n","\n").replace("\\t","\t").replace('\\"','"').replace("\\\\","\\")

print(argv)
sep = ""

if def_dir[-1] != "/":
	sep = "/"

elif def_dir[-1] != "\\":
	sep = "\\"

draw (string, def_dir + sep + animal + ".txt")