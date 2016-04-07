def main ():

	import sys
	inFile = sys.argv[1] #Arxiu entrada
	f = open(inFile,'r') #Obro arxiu
	hangar = []
	for line in f:
		splited = line.split( )
		hangar.append(splited[1])
	f.close() #Tanco arxiu

	llista = map(int, hangar) #Passa a una llista d'integers
	llista.sort() #Ordena la llista
	#print llista
	posicio = 0
	posicio = obtindre(llista,posicio)
	print "Solution: " + str(posicio) 		

def obtindre(llista,posicio):

		if(llista[0]==posicio):
			return obtindre(llista[1:],posicio+1)
		else: 
			return posicio

if __name__ == "__main__":
	main();

#Practica1 Forma Recursiva_Final
