import random


class Car:
    def __init__(self, r, m):
        self.reg_number = r
        self.max_speed = m
        self.current_speed = 0
        self.trav_distance = 0

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if change_of_speed < 0:
            self.current_speed = max(0, new_speed)
        else:
            self.current_speed = min(new_speed, self.max_speed)

    def drive(self, num_of_hours):
        new_travel_distance = (num_of_hours * self.current_speed)
        self.trav_distance += new_travel_distance


class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.distance = kilometers
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            accelerate = random.randint(-10, 15)
            car.accelerate(accelerate)
            car.drive(1)

    def print_status(self):
        print("-------------------------------------------------------------")
        print(f"Race: {self.name} ({self.distance} km)")
        print("-------------------------------------------------------------")
        print(f"Reg Num\t|\tMax Speed\t|\tCurrent Speed\t|\tDistance\t|")
        print("-------------------------------------------------------------")
        for car in self.cars:
            print(
                f"{car.reg_number.ljust(10)}|\t{car.max_speed}\t\t|\t{car.current_speed}\t\t\t|\t{car.trav_distance}\t\t|")
        print("-------------------------------------------------------------")

    def race_finished(self):
        for car in self.cars:
            if car.trav_distance >= self.distance:
                return True
        return False


car_list = [Car(f"ABC-{i}", random.randint(100, 200)) for i in range(1, 11)]

grand_demolition_derby = Race("Grand Demolition Derby", 8000, car_list)

hour = 0
while not grand_demolition_derby.race_finished():
    grand_demolition_derby.hour_passes()
    hour += 1

    # Print status every ten hours
    if hour % 10 == 0:
        grand_demolition_derby.print_status()

grand_demolition_derby.print_status()
