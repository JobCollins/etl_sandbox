from abstract_factory import AbstractFactory


def client_code(factory: AbstractFactory) -> None:

    car = factory.createCar()
    bike = factory.createBike()

    print(f"{bike.turn()}")
    print(f"{bike.honk()}", end="")