import pandas as pd
import datetime
from gasolineBus import GasolineBus
from electricBus import ElectricBus


class Model:
    controller = None

    def __init__(self):
        self.df = None

    def __del__(self):
        del self.df

    def set_controller(self, controller):
        self.controller = controller

    def get_reg_nbs(self, col):
        self.df = pd.read_csv('reg_nbs.csv', sep=';')
        return self.df[col]

    def update_bus(self, registration_nb, location, mileage, fuel_level):
        if not mileage.isnumeric():
            self.controller.update_view("Mileage is not a number")
        if not fuel_level.isnumeric():
            self.controller.update_view("Fuel level is not a number")
        else:
            df_new = pd.DataFrame({'registration_nb': [registration_nb], 'location': [location], 'mileage': [mileage],
                                   'fuel_level': [fuel_level], 'date': [datetime.datetime.now().date()],
                                   'time': [datetime.datetime.now().time()]})
            df_new.to_csv('busDb.csv', sep=';', index=False, mode='a', header=False)
            self.controller.update_view("Data was updated")

            self.df = pd.read_csv('reg_nbs.csv', sep=';')
            reg_column = self.df[self.df['registration_nb'] == registration_nb]
            if reg_column['type'].tolist()[0] == 'g':
                bus = GasolineBus(registration_nb, location, mileage, fuel_level)
                fuel_consumption = bus.calculate_fuel_consumption(reg_column['tank_capacity'].tolist()[0])
                print(bus, end=" ")
                print(f"i na ostatniej trasie zużył {str(fuel_consumption)}")
                self.controller.update_energy_usage(f"na ostatniej trasie zużył na km {fuel_consumption}")
            elif reg_column['type'].tolist()[0] == 'e':
                bus = ElectricBus(registration_nb, location, mileage, fuel_level)
                fuel_consumption = bus.calculate_fuel_consumption(reg_column['tank_capacity'].tolist()[0])
                print(bus, end=" ")
                self.controller.update_energy_usage(f"na ostatniej trasie zużył na km {fuel_consumption}")
