class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        print(f"{self.name.title()} is now rollover")

dog = Dog('james', 3)
other_dog = Dog('lucy', 6)

print(f"My {dog.age}-years-old dog's name is {dog.name.title()}")
dog.sit()

print(f"\nHer {other_dog.age}-years-old dog's name is {other_dog.name.title()}")
other_dog.roll_over()