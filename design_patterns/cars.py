from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def accelerate(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass

class RaceCar(Car):

    def accelerate(self) -> str:
        return "Accelerate really fast"
    
    def stop(self) -> str:
        return "Stop really fast"
    

class VintageCar(Car):

    def accelerate(self) -> str:
        return "Accelerate really slowly"
    
    def stop(self) -> str:
        return "Stop really slowly"