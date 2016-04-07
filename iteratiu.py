import sys

def main ():
	tractament_parametres()

def tractament_parametres():
	if(len(sys.argv) != 2):
		print "[Info] Us: python iteratiu.py [fitxer-arribades]"
		print "Llegint d'entrada standard."
		llegir_entrada_standard()
	else:
		llegir_fitxer()

def llegir_entrada_standard():
	print #TODO

def llegir_fitxer():
	fitxer = sys.argv[1]
	hangar = open(fitxer,'r')
	for line in hangar:
		splited = line.split()
		print splited
		#hangar.append(splited[1])
	hangar.close()

if __name__ == "__main__":
	main();
