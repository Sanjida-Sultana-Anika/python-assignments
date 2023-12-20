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


new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print(f"The current speed of car: {new_car.current_speed} km/h.")

new_car.accelerate(-200)
print(f"The current speed of car: {new_car.current_speed} km/h.")
