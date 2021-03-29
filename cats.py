class Cat:
    species = 'mammal'
    def __init__(self, name, age, weight, strike, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.strike = strike
        self.gender = gender


cat1 = Cat("Bootsie", 4, 7, 10, "Male")
cat2 = Cat("Sophie", 9, 11, 8, "Female")
cat3 = Cat("Ponce", 2, 7, 6, "Male")


def get_oldest(*args):
    return max(args)


print(f"The oldest cat, {get_oldest(cat1.name, cat2.name, cat3.name)} is {get_oldest(cat1.age, cat2.age, cat3.age)} years old.")

