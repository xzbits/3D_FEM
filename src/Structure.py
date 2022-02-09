from src.Node import Node
from src.Element import Element
import numpy as np


class Structure:
    def __init__(self):
        self.nodes = []
        self.elements = []

    def add_node(self, x1, x2, x3):
        node = Node(x1, x2, x3)
        self.nodes.append(node)
        return self.get_node(self.get_no_node()-1)

    def add_element(self, e, a, n1, n2):
        node1 = self.nodes[n1]
        node2 = self.get_node(n2)
        dummy = Element(e, a, node1, node2)
        self.elements.append(dummy)
        return self.get_element(self.get_no_element()-1)

    def get_no_node(self):
        return len(self.nodes)

    def get_node(self, idx):
        node = self.nodes[idx]
        return node

    def get_no_element(self):
        return len(self.elements)

    def get_element(self, idx):
        element = self.elements[idx]
        return element

    def enumerate_dof(self):
        start = 0
        for i in range(0, self.get_no_node()):
            start = self.get_node(i).enumerate_dof(start)
        for i in range(0, self.get_no_element()):
            self.elements[i].enumerate_dof()
        return start

    def assemble_load_vector(self):
        Neqn = self.enumerate_dof()
        dummy = (Neqn, 1)
        rg = np.zeros(dummy)
        for i in range(0, self.get_no_node()):
            dof = self.get_node(i).get_dof_number()
            f = self.get_node(i).get_force()
            for j in range(0, 3):
                r_index = dof[j]
                if r_index != -1:
                    rg[r_index] = rg[r_index] + f.get_component(j)
        return rg

    def assemble_stiffness_matrix(self):
        Neqn = self.enumerate_dof()
        dummy = (Neqn, Neqn)
        kg = np.zeros(dummy)
        for i in range(0, self.get_no_element()):
            e_dof = self.get_element(i).get_dof_number()
            ke = self.get_element(i).compute_stiffness_matrix()
            for j in range(0, 6):
                for k in range(0, 6):
                    matrix_index1 = e_dof[j]
                    matrix_index2 = e_dof[k]
                    if matrix_index1 != -1 and matrix_index2 != -1:
                        kg[matrix_index1][matrix_index2] = kg[matrix_index1][matrix_index2] + ke[j][k]
        return kg

    def select_displacement(self, ug):
        dummy = (self.get_no_node(), 3)
        dispNode = np.zeros(dummy)
        for i in range(0, self.get_no_node()):
            dof = self.get_node(i).get_dof_number()
            print(dof)
            for j in range(0, 3):
                if dof[j] != -1:
                    dispNode[i][j] = ug[dof[j]]
        return dispNode

    def solve(self):
        self.enumerate_dof()
        kg = self.assemble_stiffness_matrix()
        rg = self.assemble_load_vector()
        u = np.linalg.solve(kg, rg)
        return u

    def print(self):
        print(self.solve())
        print(self.select_displacement(self.solve()))
