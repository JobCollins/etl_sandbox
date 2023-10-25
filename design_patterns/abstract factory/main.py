from abstract_factory import RaceFactory, VintageFactory
from client_code import client_code


if __name__ == "__main__":

    print("Client: checks product style")
    client_code(RaceFactory())

    print("\n")

    print("Client: checks product style")
    client_code(VintageFactory())