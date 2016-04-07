import sys

def main ():
	tractament_parametres()

def tractament_parametres():
	if(len(sys.argv) != 2):
		print "[Info] Us: python iteratiu.py [fitxer-arribades]"
		print "Llegint d'entrada standard."
		llegir_entrada_standard()
	else:
		escriure_sortida_standard()

def llegir_entrada_standard():
	print #TODO

def escriure_sortida_standard():
	print #TODO

if __name__ == "__main__":
	main();
