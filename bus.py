from abc import ABC, abstractmethod


class Bus(ABC):
    def __init__(self, registration_nb, location, mileage, fuel_level):
        self.__registration_nb = registration_nb
        self.__location = location
        self.__mileage = mileage
        self.__fuel_level = fuel_level

    def get_registration_nb(self):
        return self.__registration_nb

    def __len__(self):
        return len(self.__registration_nb)

    def get_location(self):
        return self.__location

    def get_mileage(self):
        return self.__mileage

    def get_fuel_level(self):
        return self.__fuel_level

    def __str__(self):
        return (
            f"Autobus o numerze rejestracyjnym {self.__registration_nb} (jej długość: {len(self)}) "
            f"jest w zajezdni {self.__location}, ma przebieg {self.__mileage} i poziom paliwa {self.__fuel_level}")

    @abstractmethod
    def calculate_fuel_consumption(self, tank_capacity):
        pass
