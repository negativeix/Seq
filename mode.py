import random

class Mode:
    def __init__(self):
        self.level = 1
        self.sequence = []
        self.generate_sequence()

    def generate_sequence(self):
        self.sequence = [random.randint(0, 8) for _ in range(3)]

    def add_to_sequence(self):
        if self.level >= 4:
            new_number = random.randint(0, 8)
            self.sequence.append(new_number)

    def next_level(self):
        self.level += 1
        self.add_to_sequence()

    def get_sequence(self):
        return self.sequence

    def reset(self):
        self.level = 1
        self.generate_sequence()
