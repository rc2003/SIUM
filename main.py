import uuid

def get_people():
	people = []
	while True:
		try:
			n = int(input("How many people (1-10)? "))

			if n <= 0 or n > 10:
				print("You must insert a number of people between 1 and 10")
			else:
				for i in range(n):
					print("-------------------------")
					people.append({
						"id": uuid.uuid1(),
						"name": input("Name: "),
						"surname": input("Surname: "),
						"age": input("Age: ")
					})
				return people
		except:
			print("Something went wrong with your input")

people = get_people()

csv = "id,name,surname,age"

for p in people:
	csv += "\n{},{},{},{}".format(p["id"], p["name"], p["surname"], p["age"])

f = open("people.csv", "w")
f.write(csv)
f.close()