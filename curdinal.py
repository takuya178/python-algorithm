class Animal:
    def __init__(self, species: str, weightKg: int, heightM: int, predator: bool):
        self.species = species
        self.weightKg = weightKg
        self.heightM = heightM
        self.predator = predator

    def domesticate(self):
        self.predator = False
        return self.predator

class Hunter:
    def __init__(self, name: str, weightKg: int, heighM: int, strength: int, cageCubicMeters: int):
        self.name = name
        self.weightKg = weightKg
        self.heighM = heighM
        self.strength = strength
        self.cageCubicMeters = cageCubicMeters

    def strengthKg(self) -> int:
        return self.strength * self.weightKg

    def canCaptureAnimal(self, animal: Animal) -> bool:
        return self.strengthKg() >= animal.weightKg and self.cageCubicMeters >= animal.heightM and not animal.predator

    def attemptToDomesticate(self, animal: Animal) -> bool:
        if self.strengthKg() > animal.weightKg * 2:
            return animal.domesticate()

tiger = Animal("Tiger", 290, 2.6, True)
cow = Animal("Cow", 1134, 1.5, False)
snake = Animal("Snake", 100, 1.2, True)
cat = Animal("Cat", 10, 0.5, False)
hunternator = Hunter("Hunternator", 124.73, 1.85, 15, 3)
animals = [tiger, cow, snake, cat]

def capturedAnimals(hunternator: Hunter, animals: list):
    for i in range(len(animals)):
        if hunternator.canCaptureAnimal(animals[i]):
            print(animals[i].species)


def domesticateTheAnimals(hunternator: Hunter, animals: list) -> list:
    for i in range(len(animals)):
        hunternator.attemptToDomesticate(animals[i])
    return animals

capturedAnimals(hunternator, animals)

domesticateTheAnimals(hunternator, animals)
capturedAnimals(hunternator, animals)



