import math
import numpy as np


class Element:
    def __init__(self, e, a, n1, n2):
        self.e = e
        self.a = a
        self.n1 = n1
        self.n2 = n2
        self.dof_numbers = [0, 0, 0, 0, 0, 0]

    def compute_stiffness_matrix(self):
        ke1 = np.outer(self.get_e1(), self.get_e1())
        dummy = (6, 6)
        ke = np.zeros(dummy)
        eal = self.get_area() * self.get_e_modulus() / (self.get_length() ** 3)
        for i in range(0, 3):
            for j in range(0, 3):
                ke[i][j] = ke1[i][j] * eal

        for i in range(0, 3):
            for j in range(3, 6):
                ke[i][j] = ke1[i][j - 3] * eal * (-1)

        for i in range(3, 6):
            for j in range(0, 3):
                ke[i][j] = ke1[i - 3][j] * eal * (-1)

        for i in range(3, 6):
            for j in range(3, 6):
                ke[i][j] = ke1[i - 3][j - 3] * eal
        return ke

    def get_dof_number(self):
        return self.dof_numbers

    def enumerate_dof(self):
        node1 = self.get_node1()
        node2 = self.get_node2()

        for i in range(0, len(self.dof_numbers)):
            if i <= 2:
                self.dof_numbers[i] = node1.get_dof_number()[i]

            if i > 2:
                self.dof_numbers[i] = node2.get_dof_number()[i - 3]

    def get_e1(self):
        x1 = self.n1.get_position()
        x2 = self.n2.get_position()
        v12 = [x2[0] - x1[0], x2[1] - x1[1], x2[2] - x1[2]]
        return v12

    def get_length(self):
        length = math.sqrt((self.get_e1()[0] ** 2) + (self.get_e1()[1] ** 2) + (self.get_e1()[2] ** 2))
        return length

    def get_node1(self):
        return self.n1

    def get_node2(self):
        return self.n2

    def get_area(self):
        return self.a

    def get_e_modulus(self):
        return self.e

    def print(self):
        print(self.get_e_modulus(), self.get_area(), self.get_length())

    def print_enu(self):
        print(self.dof_numbers)
