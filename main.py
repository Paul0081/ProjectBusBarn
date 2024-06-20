from view import View
from model import Model
from controller import Controller
from electricBus import ElectricBus
import gc

if __name__ == "__main__":
    view = View()
    model = Model()
    controller = Controller(model, view)
    view.set_controller(controller)
    model.set_controller(controller)
    view.show_main_window()
    # Garbage Collector
    # gc.collect()
    print("KONIEC PROGRAMU")

    bus1 = ElectricBus('opo1234', 'Opole', 22, 33)
    bus2 = ElectricBus('opo5678', 'Opole', 11, 12)
    bus3 = bus1 + bus2
    print(bus3)
