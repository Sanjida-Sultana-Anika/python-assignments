class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.trav_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if change_of_speed < 0:
            self.current_speed = max(0, new_speed)
        else:
            self.current_speed = min(new_speed, self.max_speed)

    def drive(self, num_of_hours):
        new_travel_distance = num_of_hours * self.current_speed
        self.trav_distance += new_travel_distance


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, battery_capacity):
        super().__init__(reg_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, tank_volume):
        super().__init__(reg_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC- 15", 180, 52.5)
gasoline_car = GasolineCar("ACD- 123", 165, 32.3)

electric_car.accelerate(50)
gasoline_car.accelerate(40)

electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric Car- Registration Number: {electric_car.reg_number}, Distance Traveled: {electric_car.trav_distance} km")
print(f"Gasoline Car- Registration Number: {gasoline_car.reg_number}, Distance Traveled: {gasoline_car.trav_distance} km")
