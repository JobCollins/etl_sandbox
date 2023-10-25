from abc import ABC, abstractmethod


class Bike(ABC):

    @abstractmethod
    def turn(self) -> str:
        pass

    @abstractmethod
    def honk(self) -> str:
        pass


class RaceBike(Bike):
    def turn(self) -> str:
        return "Turn really fast"
    
    def honk(self) -> str:
        return "Honk loudly"
    
class VintageBike(Bike):
    def turn(self) -> str:
        return "Turn really slowly"
    
    def honk(self) -> str:
        return "Honk quietly"