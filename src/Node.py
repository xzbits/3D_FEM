from src.Constraint import Constraint
from src.Force import Force


class Node:
    def __init__(self, x1, x2, x3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3

        # create additional attributes of node
        self.coordinate = [x1, x2, x3]
        self.dofNumbers = [-1, -1, -1]
        self.displacement = [0.0, 0.0, 0.0]

        # create force and constraint
        self.constraint = Constraint(True, True, True)
        self.force = Force(0.0, 0.0, 0.0)

    def set_constraint(self, con):
        self.constraint = con

    def get_constraint(self):
        return self.constraint

    def set_force(self, forces):
        self.force = forces

    def get_force(self):
        return self.force

    def enumerate_dof(self, start):
        u1 = self.get_displacement()[0]
        u2 = self.get_displacement()[1]
        u3 = self.get_displacement()[2]
        for i in range(0, len(self.dofNumbers)):
            if self.get_constraint().is_free(i) == False or u1 != 0 or u2 != 0 or u3 != 0:
                self.dofNumbers[i] = -1
            else:
                self.dofNumbers[i] = start
                start += 1
        return start

    def get_dof_number(self):
        return self.dofNumbers

    def set_displacement(self, a, b, c):
        disp = [a, b, c]
        self.displacement = disp
        return self.displacement

    def get_displacement(self):
        v3 = [self.displacement[0], self.displacement[1], self.displacement[2]]
        return v3

    def get_position(self):
        v3 = [self.x1, self.x2, self.x3]
        return v3

    def print(self):
        print(self.coordinate)
