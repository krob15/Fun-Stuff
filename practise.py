import math
pet_cuteness_data = [["George", "dog", "Bob", 4],
                    ["Luna", "cat", "Bob", 42],
                    ["Coco", "cat", "Jane", 52],
                    ["Max", "dog", "Alice", 74],
                    ["Oliver", "cat", "Fred", 70],
                    ["Cooper", "dog","Fred", 60],
                    ["Oscar", "cat", "Bob", 30],
                    ["Bella", "cat", "Fred", 48],
                    ["Charlie", "cat", "Fred",32],
                    ["Milo", "dog", "Bob", 50],
                    ["Buddy", "dog", "Alice", 18],
                    ["Teddy", "dog", "Fred", 48],
                    ["Rocky", "dog", "Jane", 54],
                    ["Bear", "dog", "Jane", 68],
                    ["Lily", "cat", "Fred", 62],
                    ["Kitty", "cat","Alice", 46],
                    ["Leo", "dog", "Alice", 44],
                    ["Lucy", "cat","Fred", 58],
                    ["Loki", "cat", "Alice", 72],
                    ["Duke", "dog", "Jane", 70]]
class Pets:
    def __init__(self, name, species, owner, cute_score):
        self.name = name
        self.species = species
        self.owner = owner
        self.cute_score = cute_score

pets =  [Pets(pet_data[0], pet_data[1], pet_data[2], pet_data[3]) for pet_data in pet_cuteness_data]

pet_function = pets.copy()

def average_cuteness(pets):
    return(round(sum(pets)/len(pets)), 0)


