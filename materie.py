max_materie = 3
materie = int(input("Inserisci numero di materie: "))
print("------------------------------------------")

if materie > max_materie:
	print("Superato numero massimo di materie possibili")
	exit()

file = open("MATERIE.csv", "w+")
file.write("IDMateria, Materia")

materia=dict()

for b in range(materie):
	materia["IDMateria"] = input("Inserisci il numero di materia: ")
	materia["Materia"] = input("Inserisci il nome della materia: ")
	print("------------------------------------------")
	file.write("\n"+materia["IDMateria"]+", "+materia["Materia"])
