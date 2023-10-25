from abc import ABC, abstractmethod

class RobotBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_head(self):
        pass

    @abstractmethod
    def build_arms(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass

    @abstractmethod
    def build_torso(self):
        pass

    @abstractmethod
    def build_battery(self):
        pass

    @abstractmethod
    def get_robot(self):
        pass