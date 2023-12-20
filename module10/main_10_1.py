class Elevator:
    def __init__(self, num_bf, num_tf):
        self.current_floor = 0
        self.num_bottom_floor = num_bf
        self.num_top_floor = num_tf

    def go_to_floor(self, destination_floor):
        if destination_floor < self.current_floor:
            for i in range(0, self.current_floor - destination_floor):
                self.floor_down()
        elif destination_floor > self.current_floor:
            for i in range(0, destination_floor - self.current_floor):
                self.floor_up()

    def floor_up(self):
        if self.current_floor < self.num_top_floor:
            self.current_floor += 1
        print(f"The elevator is at floor: {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.num_bottom_floor:
            self.current_floor -= 1
        print(f"The elevator is at floor: {self.current_floor}")


h = Elevator(-1, 10)
h.go_to_floor(5)
h.go_to_floor(0)
