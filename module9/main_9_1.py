class Car:
    def __init__(self, r, m):
        self.reg_number = r
        self.max_speed = m
        self.current_speed = 0
        self.trav_distance = 0


new_car = Car("ABC-123", 142)
print(f"Car details: \n"
      f"Registration number: {new_car.reg_number}\n"
      f"Maximum speed:       {new_car.max_speed} km/h\n"
      f"Current speed:       {new_car.current_speed}\n"
      f"Distance travelled:  {new_car.trav_distance}")
