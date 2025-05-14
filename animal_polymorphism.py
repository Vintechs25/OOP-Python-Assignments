# Base Animal Class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Dog Class (Subclass of Animal)
class Dog(Animal):
    def move(self):
        print("The dog is running!")

# Bird Class (Subclass of Animal)
class Bird(Animal):
    def move(self):
        print("The bird is flying!")

# Fish Class (Subclass of Animal)
class Fish(Animal):
    def move(self):
        print("The fish is swimming!")

# Demonstrating Polymorphism
def make_move(animal):
    animal.move()

# Example Usage
dog = Dog()
bird = Bird()
fish = Fish()

make_move(dog)  # Output: The dog is running!
make_move(bird)  # Output: The bird is flying!
make_move(fish)  # Output: The fish is swimming!
