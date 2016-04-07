def main ():
	
	import sys
	inFile = sys.argv[1] #Arxiu entrada
	hangar = []
	f = open(inFile,'r') #Obro arxiu
	for line in f:
		splited = line.split( )
		hangar.append(splited[1])
	f.close() #Tanco arxiu

	llista = map(int, hangar) #Passa a una llista d'integers
	llista.sort() #Ordena la llista
	posicio = 0
	trobat = False
	while(posicio<len(llista) and trobat == False):
		
		if(posicio == llista[posicio]): posicio = posicio + 1
		else: trobat = True

	print "Solution: " + str(posicio)	
	

if __name__ == "__main__":
	main();

#Practica1 Forma Iterativa
