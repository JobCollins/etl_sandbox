"""
The first thing the Abstract Factory recommends is to explicitly declare interfaces (classes that cannot be instantiated) for each product, 
for example for a car and a bike product. Then you can have all product variants implement the interfaces so we are sure they will share 
attributes and functions that are common to all objects , such as accelerate() and stop().

"""

from __future__ import annotations
from abc import ABC, abstractmethod

from cars import RaceCar, VintageCar
from bike import RaceBike, VintageBike

class AbstractFactory(ABC):

    @abstractmethod
    def createCar(self) -> Car:
        pass

    @abstractmethod
    def createBike(self) -> Bike:
        pass


class RaceFactory(AbstractFactory):

    def createCar(self) -> Car:
        return RaceCar()
    
    def createBike(self) -> Bike:
        return RaceBike()
    

class VintageFactory(AbstractFactory):

    def createCar(self) -> Car:
        return VintageCar()
    
    def createBike(self) -> Bike:
        return VintageBike()
    
