class Force:
    def __init__(self, r1, r2, r3):
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        # create component
        self.component = [r1, r2, r3]

    def get_component(self, c):
        return self.component[c]

    def print(self):
        print(self.component)
