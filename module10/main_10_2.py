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


class Building:
    def __init__(self, nbf, ntf, n_elevators):
        self.bottom_floor = nbf
        self.top_floor = ntf
        self.all_elevators = [Elevator(nbf, ntf) for _ in range(n_elevators)]

    def run_elevator(self, n_elevator, des_floor):
        if 0 <= n_elevator < len(self.all_elevators):
            elevator = self.all_elevators[n_elevator]
            elevator.go_to_floor(des_floor)
        else:
            print("Invalid elevator number")


new_building = Building(-1, 10, 2)
new_building.run_elevator(0, 5)
