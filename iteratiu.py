import sys

places_ocupades = []

def main ():
	tractament_parametres()

def tractament_parametres():
	if(len(sys.argv) != 2):
		print "[Info] Us: python iteratiu.py [fitxer-arribades]"
		llegir_entrada_standard()
		parametres = False
		llegir_fitxer(parametres)
		buscar_lloc()
	else:
		try:
			parametres = True
			llegir_fitxer(parametres)
			buscar_lloc()
		except IOError:
			print "[Error] No s'ha pogut trobar el fitxer especificat."


def llegir_entrada_standard():
	new_hangar = open("landings.txt", 'w')
	print "[Info] Introdueix una llista amb format: 'nom-nau' 'posicio-hangar'"
	print "[Info] Per acabar, prem [Enter] en una linea en blanc."
	acabat = False
	while (acabat != True):
		llista = raw_input()
		if(llista == ""):
			acabat = True
		else:
			new_hangar.write(llista + "\n")

def llegir_fitxer(parametres):
	if(parametres == True):
		fitxer = sys.argv[1]
	else:
		fitxer = 'landings.txt'
	hangar = open(fitxer,'r')
	for linea in hangar:
		splited = linea.split( )
 		places_ocupades.append(splited[1])
	hangar.close()

def buscar_lloc():
	places_ocupades_int = map(int, places_ocupades)
	places_ocupades_asc = quicksort(places_ocupades_int)
	print places_ocupades_asc

	posicio = 0
	trobat = False

	while(posicio<len(places_ocupades_asc) and trobat == False):
 		if(posicio == places_ocupades_asc[posicio]): posicio = posicio + 1
 		else: trobat = True

 	print "Solution: " + str(posicio)


def quicksort(llista_places):
	if llista_places == []: return []
	return quicksort([x for x in llista_places[1:] if x< llista_places[0]]) + llista_places[0:1] + \
		quicksort([x for x in llista_places[1:] if x>=llista_places[0]])



if __name__ == "__main__":
	main();
