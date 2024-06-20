from bus import Bus


class ElectricBus(Bus):

    def calculate_fuel_consumption(self, tank_capacity):
        fuel_consumption = 100 - float(self.get_fuel_level())
        used_energy = fuel_consumption / 100 * tank_capacity
        energy_per_km = used_energy / float(self.get_mileage())
        return str(round(energy_per_km, 3)) + " kWh"

    def __add__(self, bus2):
        return ElectricBus("Powstał autobus przegubowy", self.get_location(), self.get_mileage() + bus2.get_mileage(),
                           self.get_fuel_level() + bus2.get_fuel_level())
