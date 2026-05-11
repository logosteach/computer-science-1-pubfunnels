# -- snip --
# import statement
# Animal, ZooEmployee, and Zookeeper class code goes here
# -- snip --

class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def buy_ticket(self):
        print(f"{self.name} bought a ticket.")

class ChildVisitor(Visitor):
    def __init__(self, name, age, favorite_animal):
        super().__init__(name, age)
        self.favorite_animal = favorite_animal

    def buy_ticket(self):
        print(f"{self.name} (age {self.age}) bought a discounted child ticket.")

    def share_favorite(self):
        print(f"My favorite is {self.favorite_animal}!")

# Main code
adult = Visitor("John", 30)
adult.buy_ticket()
kid = ChildVisitor("Lily", 8, "Panda")
kid.buy_ticket()
kid.share_favorite()
