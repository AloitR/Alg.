import sys

def main ():
	tractament_parametres()

def tractament_parametres():
	if(len(sys.argv) != 2): # En cas de no haber parametres d'entrada
		print "[Info] Us: python iteratiu.py [fitxer-arribades]"
		llegir_entrada_standard()
		parametres = False
		llegir_fitxer(parametres)
		buscar_lloc()
	else: #En cas d'haber parametres d'entrada
		try:
			parametres = True
			llegir_fitxer(parametres)
			buscar_lloc()
		except IOError:
			print "[Error] No s'ha pogut trobar el fitxer especificat."
			# Tractament d'error en cas de fitxer inexistent.

def llegir_entrada_standard():
	print # TODO
def llegir_fitxer(parametres):
	print # TODO
def buscar_lloc():
	print # TODO

if __name__ == "__main__":
	main();
