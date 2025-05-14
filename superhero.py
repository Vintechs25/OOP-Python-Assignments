# Superhero Class
class Superhero:
    def __init__(self, name, power, alias):
        self.name = name  # Hero's real name
        self.power = power  # Superpower
        self.alias = alias  # Hero's alias

    def display_info(self):
        return f"Superhero {self.name}, also known as {self.alias}, has the power of {self.power}."

    def save_the_day(self):
        print(f"{self.alias} is saving the day!")

# Villain Class (Inheritance Example)
class Villain(Superhero):
    def __init__(self, name, power, alias, evil_plan):
        super().__init__(name, power, alias)
        self.evil_plan = evil_plan  # Villain's evil plan

    def display_info(self):
        return f"Villain {self.name}, known as {self.alias}, has the power of {self.power} and plans to {self.evil_plan}."

    def destroy(self):
        print(f"{self.alias} is executing their evil plan: {self.evil_plan}!")

# Example Usage
hero = Superhero("Clark Kent", "Super Strength", "Superman")
villain = Villain("Lex Luthor", "Genius Intellect", "Lex Luthor", "take over the world")

print(hero.display_info())
hero.save_the_day()

print(villain.display_info())
villain.destroy()
