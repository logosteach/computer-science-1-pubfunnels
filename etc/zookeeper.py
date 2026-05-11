from abc import ABC, abstractmethod

# -- snip --
# Animal Class code goes here
# -- snip --

class ZooEmployee(ABC):
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @abstractmethod
    def perform_duty(self):
        pass

    def introduce(self):
        print(f"Hi, I'm {self.name}, the {self.role}.")

class Zookeeper(ZooEmployee):
    def perform_duty(self):
        print(f"{self.name} is feeding the animals.")

# Main code
# employee = ZooEmployee("Bob", "Manager")  # This will raise TypeError!
keeper = Zookeeper("Alice", "Zookeeper")
keeper.introduce()
keeper.perform_duty()
