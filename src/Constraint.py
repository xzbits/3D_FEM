class Constraint:
    def __init__(self, u1, u2, u3):
        self.u1 = u1
        self.u2 = u2
        self.u3 = u3

        # create list of constraints
        self.free = [u1, u2, u3]

    def is_free(self, idx):
        return self.free[idx]

    def print(self):
        print(self.free)
