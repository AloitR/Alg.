import sys

places_ocupades = []

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
	new_hangar = open("landings.txt", 'w') # No parametre -> arxiu per defecte.
	print "[Info] Introdueix una llista amb format: 'nom-nau' 'posicio-hangar'"
	print "[Info] Per acabar, prem [Enter] en una linea en blanc."
	acabat = False
	while (acabat != True): #Anar llegint i escribint d'entrada standard.
		llista = raw_input()
		if(llista == ""):
			acabat = True
		else:
			new_hangar.write(llista + "\n")

def llegir_fitxer(parametres):
	if(parametres == True): # En cas d'haber parametre d'entrada usará aquest.
		fitxer = sys.argv[1]
	else:					# En cas contrari en creeem un i l'utilitzem.
		fitxer = 'landings.txt'
	hangar = open(fitxer,'r')
	for linea in hangar:			# Llegir totes les linees i tractarles.
		splited = linea.split( )			# "Nau 1" 	 -> ["Nau","1"]
 		places_ocupades.append(splited[1])	# ["Nau","1"]-> ["1"]
	hangar.close()

def buscar_lloc():
	places_ocupades_int = map(int, places_ocupades) # ["1"] -> [1]
	places_ocupades_asc = quicksort(places_ocupades_int) # Ordenar amb Quicksort
	print places_ocupades_asc

	posicio = 0
	trobat = False

	#Anar recorrent mentres pos i contingut coincideixin
	while(posicio<len(places_ocupades_asc) and trobat == False):
 		if(posicio == places_ocupades_asc[posicio]): posicio = posicio + 1
 		else: trobat = True

 	print "Solution: " + str(posicio)

# Funció recursiva Quicksort per tal de no usar .sort()
def quicksort(llista_places):
	if llista_places == []: return []
	return quicksort([x for x in llista_places[1:] if x< llista_places[0]]) + llista_places[0:1] + \
		quicksort([x for x in llista_places[1:] if x>=llista_places[0]])

if __name__ == "__main__":
	main();
