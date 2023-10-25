# Client code
from concrete_builder import DroneRobotBuilder, HumanoidRobotBuilder, RobotDirector


if __name__ == "__main__":
    director = RobotDirector()

    humanoid_builder = HumanoidRobotBuilder()
    director.set_builder(humanoid_builder)
    humanoid_robot = director.build_humanoid_robot()

    drone_builder = DroneRobotBuilder()
    director.set_builder(drone_builder)
    drone_robot = director.build_drone_robot()

    print("Humanoid Robot Components:")
    print(f"Head: {humanoid_robot.head}")
    print(f"Arms: {humanoid_robot.arms}")
    print(f"Legs: {humanoid_robot.legs}")
    print(f"Torso: {humanoid_robot.torso}")
    print(f"Battery: {humanoid_robot.battery}")

    print("\nDrone Robot Components:")
    print(f"Head: {drone_robot.head}")
    print(f"Arms: {drone_robot.arms}")
    print(f"Legs: {drone_robot.legs}")
    print(f"Torso: {drone_robot.torso}")
    print(f"Battery: {drone_robot.battery}")