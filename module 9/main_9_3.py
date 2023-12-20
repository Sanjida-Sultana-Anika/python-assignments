class Car:
    def __init__(self, r, m, td):
        self.reg_number = r
        self.max_speed = m
        self.current_speed = 0
        self.trav_distance = td

    def accelerate(self, change_of_speed):
        new_speed = self.current_speed + change_of_speed
        if change_of_speed < 0:
            self.current_speed = max(0, new_speed)
        else:
            self.current_speed = min(new_speed, self.max_speed)

    def drive(self, num_of_hours):
        new_travel_distance = (num_of_hours * self.current_speed)
        self.trav_distance += new_travel_distance


new_car = Car("ABC-123", 142, 2000)

print(f"The initial travel distance was: {new_car.trav_distance} km")

new_car.accelerate(60)
new_car.drive(1.5)

print(f"Your current speed is: {new_car.current_speed} km/h")
print(f"Your total travel distance is: {new_car.trav_distance} km")
