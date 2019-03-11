
class Dog:
  def __init__(self, CEP, porte=None, raca=None, contato=None):
    self.CEP = CEP
    self.porte = porte
    self.raca = raca
    self.contato = contato

lost_dogs = {}

def insert_dog(dog):
	lost_dogs[dog.CEP].append(dog)

def search_dog(CEP, porte=None, raca=None):
	dogs_set = lost_dogs[CEP]
	dogs_set_aux = []
	if not porte is None:
		for dog in dogs_set:
			if dog.porte == porte:
				dogs_set_aux.append(dog)

	dogs_set = dogs_set_aux
	if not raca is None:
	for dog in dogs_set:
		if dog.raca == raca:
			dogs_set_aux.append(dog)

	return dogs_set

