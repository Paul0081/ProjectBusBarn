from tkinter import *
from tkinter import ttk


class View:
    def __init__(self):
        self.__labelEnergyUsage = None
        self.__labelResult = None
        self.__spinBoxFuel = None
        self.__spinBoxMil = None
        self.__comboBoxReg = None
        self.__window = None
        self.__label = None
        self.__scrollBarLoc = None
        self.__listBoxLoc = None
        self.__labelFuel = None
        self.__labelMil = None
        self.__labelLoc = None
        self.__labelReg = None
        self.__button = None
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def show_main_window(self):
        self.__window = Tk()
        self.__window.title("BusBarn🚐")

        self.__labelReg = Label(text="Wybierz rejestrację: ")
        choices = list(self.controller.read_reg())
        combo_selected = StringVar()
        self.__comboBoxReg = ttk.Combobox(self.__window, textvariable=combo_selected, values=choices)

        self.__labelLoc = Label(text="Wybierz lokalizację: ")
        self.__listBoxLoc = Listbox(self.__window, height=6)
        self.__listBoxLoc.insert(1, "Gaj")
        self.__listBoxLoc.insert(2, "Grabiszyńska")
        self.__listBoxLoc.insert(3, "Ołbin")
        self.__listBoxLoc.insert(4, "Obornicka")
        self.__listBoxLoc.insert(5, "Borek")
        self.__listBoxLoc.insert(6, "Michalczewski")

        self.__labelMil = Label(text="Wpisz ilość przejechanych kilometrów: ")
        busMilValue = StringVar()
        self.__spinBoxMil = ttk.Spinbox(self.__window, from_=0, to=100000, increment=.001, textvariable=busMilValue)

        self.__labelFuel = Label(text="Wpisz ilość paliwa [%]: ")
        fuelValue = StringVar()
        self.__spinBoxFuel = ttk.Spinbox(self.__window, from_=0, to=100, increment=.01, wrap=True,
                                         textvariable=fuelValue)

        self.__button = Button(text="Prześlij", command=self.on_button_click)

        self.__labelResult = Label()

        self.__labelEnergyUsage = Label()

        self.__labelReg.pack()
        self.__comboBoxReg.pack()
        self.__labelLoc.pack()
        self.__listBoxLoc.pack()
        self.__labelMil.pack()
        self.__spinBoxMil.pack()
        self.__labelFuel.pack()
        self.__spinBoxFuel.pack()
        self.__button.pack()
        self.__window.geometry("300x320")
        self.__window.mainloop()

    def on_button_click(self):
        try:
            self.__listBoxLoc.get(self.__listBoxLoc.curselection())
            if (self.__comboBoxReg.get() or self.__spinBoxMil.get() or self.__spinBoxFuel.get()) in (None, '', []):
                self.show_update_result("Fill out empty fields")
            else:
                self.controller.update_bus(self.__comboBoxReg.get(),
                                           self.__listBoxLoc.get(self.__listBoxLoc.curselection()),
                                           self.__spinBoxMil.get(), self.__spinBoxFuel.get())
        except Exception as e:
            print(e)
            self.show_update_result("Fill in correct data")

    def show_update_result(self, message):
        self.__labelResult.config(text=message)
        self.__labelResult.pack()

    def show_energy_usage(self, message):
        self.__labelEnergyUsage.config(text=message)
        self.__labelEnergyUsage.pack()
