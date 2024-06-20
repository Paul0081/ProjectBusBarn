class Controller:
    model = None
    view = None

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def read_reg(self):
        regs = self.model.get_reg_nbs('registration_nb')
        return regs

    def update_bus(self, registration_nb, location, mileage, fuel_level):
        self.model.update_bus(registration_nb, location, mileage, fuel_level)

    def update_view(self, message):
        self.view.show_update_result(message)

    def update_energy_usage(self, message):
        self.view.show_energy_usage(message)
