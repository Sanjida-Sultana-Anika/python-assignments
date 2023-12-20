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


max_distance_driven_by_any_car = 0

car_list = []

for i in range(1, 11):
    max_speed = random.randint(100, 200)
    new_car = Car("ABC-" + str(i), max_speed)
    car_list.append(new_car)

while max_distance_driven_by_any_car < 10000:
    for car in car_list:
        accelerate = random.randint(-10, 15)
        car.accelerate(accelerate)
        car.drive(1)
        max_distance_driven_by_any_car = max(max_distance_driven_by_any_car, car.trav_distance)

print("-------------------------------------------------------------")
print(f"Reg Num\t|\tMax Speed\t|\tCurrent Speed\t|\tDistance\t|")
print("-------------------------------------------------------------")

for car in car_list:
    print(f"{car.reg_number}\t|\t\t{car.max_speed}\t\t|\t\t{car.current_speed}\t\t\t|\t{car.trav_distance}\t\t|")
print("-------------------------------------------------------------")
