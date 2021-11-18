max_record = 10
num = int(input("Inserisci il numero di matricole: "))
print("------------------------------------------")

if num > max_record:
	print("Superato numero massimo di matricole possibili")
	exit()

file = open("MATRICOLE.txt",  "w+")
file.write("IDMatricola, Cognome, Nome")

matricola=dict()

for persona in range(num):
	matricola["IDMatricola"] = input("Inserisci il numero di matricola: ")
	matricola["Cognome"] = input("Inserisci il cognome della matricola: ")
	matricola["Nome"] = input("Inserisci il nome della matricola: ")
	print("------------------------------------------")
	file.write("\n"+matricola["IDMatricola"]+", "+matricola["Cognome"]+", "+matricola["Nome"])
