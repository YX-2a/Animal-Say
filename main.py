from sys import argv
from draw import draw

args = []

for arg in argv [2:] :
	args.append (arg + " ")

if args == [] :
		print ("Syntax :\nmain_arg.py <ascci file> <words>")

else :
	draw ("".join (args), argv[1])


