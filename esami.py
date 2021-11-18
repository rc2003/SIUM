max_esami = 3
esami = int(input("Inserisci numero di esami da sostenere: "))

if esami > max_esami:
	print("Superato numero massimo di esami possibili")
	exit()

file = open("ESAMI.txt", "w+")
file.write("IDMatricola, IDMateria")

esame=dict()

for b in range(esami):
	esame["IDMatricola"] = input("Inserisci il numero di matricola: ")
	esame["IDMateria"] = input("Inserisci il numero di materia: ")
	file.write("\n"+esame["IDMatricola"]+", "+esame["IDMateria"])