from bus import Bus


class GasolineBus(Bus):

    def calculate_fuel_consumption(self, tank_capacity):
        fuel_consumption = 100 - float(self.get_fuel_level())
        used_energy = fuel_consumption / 100 * tank_capacity
        energy_per_km = used_energy / float(self.get_mileage())
        return str(round(energy_per_km, 2)) + " litrów"
