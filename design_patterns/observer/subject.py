from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update():
        #new post
        pass

class Subject(ABC):

    @abstractmethod
    def registerObserver(self, ob:Observer):
        pass

    @abstractmethod
    def unregisterObserver(self, ob:Observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass