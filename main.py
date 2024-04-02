"""Vehacle and Electric"""


class Vehacle:
    """ Main class Vehacle"""
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        """get info"""
        return f"Make is {self.make}, Model is {self.model}"


class Car(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


class Moto(Vehacle):
    def __init__(self, make, model, wheels):
        super().__init__(make, model)
        self.wheels = wheels


class Electric:
    """Electric"""
    def __init__(self):
        self.__battery = 0

    def charge(self):
        self.__battery = 100


class ElectricCar(Vehacle, Electric):
    def __init__(self, make, model, wheels):
        Vehacle.__init__(self, make, model)
        Electric.__init__(self)
        self.wheels = wheels


class ElectricMoto(Vehacle, Electric):
    def __init__(self, make, model, wheels):
        Vehacle.__init__(self, make, model)
        Electric.__init__(self)
        self.wheels = wheels


car = Car("Toyota", "Corolla", 4)
moto = Moto("Honda", "CBR600RR", 2)
el_car = ElectricCar("Tesla", "Model S", 4)
el_moto = ElectricMoto("Zero", "SR/F", 2)

print(car.get_info())
print(moto.get_info())
print(el_car.get_info())
print(el_moto.get_info())

print(Car.mro())
print(Moto.mro())
print(ElectricCar.mro())
print(ElectricMoto.mro())
