# Define a Concrete Builder for a Robot
from robot import Robot
from robot_builder import RobotBuilder


class HumanoidRobotBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()
        self.reset()

    def reset(self):
        self.robot = Robot()

    def build_head(self):
        self.robot.head = "Humanoid Head"

    def build_arms(self):
        self.robot.arms = "Humanoid Arms"

    def build_legs(self):
        self.robot.legs = "Humanoid Legs"

    def build_torso(self):
        self.robot.torso = "Humanoid Torso"

    def build_battery(self):
        self.robot.battery = "Humanoid Battery"

    def get_robot(self):
        return self.robot
# Define a Concrete Builder for a Robot
class DroneRobotBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()
        self.reset()

    def reset(self):
        self.robot = Robot()

    def build_head(self):
        self.robot.head = "Drone Head"

    def build_arms(self):
        self.robot.arms = "No Arms"

    def build_legs(self):
        self.robot.legs = "No Legs"

    def build_torso(self):
        self.robot.torso = "Drone Torso"

    def build_battery(self):
        self.robot.battery = "Drone Battery"

    def get_robot(self):
        return self.robot
    

# Define the RobotDirector class with methods to create different robots
class RobotDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_humanoid_robot(self):
        self.builder.reset()
        self.builder.build_head()
        self.builder.build_arms()
        self.builder.build_legs()
        self.builder.build_torso()
        self.builder.build_battery()
        return self.builder.get_robot()

    def build_drone_robot(self):
        self.builder.reset()
        self.builder.build_head()
        self.builder.build_torso()
        self.builder.build_battery()
        return self.builder.get_robot()