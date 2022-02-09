import numpy as np
import math
from src.Structure import Structure
from src.Force import Force
from src.Constraint import Constraint

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    struct = Structure()
    lb = 15.0
    r = 457.2 / 2000
    t = 10.0 / 1000
    a = np.pi * (np.power(r, 2) - np.power(r - t, 2))
    e = 2.1e11
    c1 = Constraint(False, False, False)
    c2 = Constraint(True, True, False)
    f = Force(0, -20e3, -100e3)

    # create nodes
    n1 = struct.add_node(0.0, 0.0, lb * np.sqrt(2.0 / 3.0))
    n2 = struct.add_node(0.0, lb / math.sqrt(3), 0)
    n3 = struct.add_node(-lb / 2, -lb / math.sqrt(12.0), 0)
    n4 = struct.add_node(lb / 2, -lb / math.sqrt(12.0), 0)

    # apply BCs
    n1.set_force(f)
    n2.set_constraint(c1)
    n3.set_constraint(c1)
    n4.set_constraint(c2)

    # create elements
    struct.add_element(e, a, 0, 1)
    struct.add_element(e, a, 0, 2)
    struct.add_element(e, a, 0, 3)
    struct.add_element(e, a, 1, 2)
    struct.add_element(e, a, 2, 3)
    struct.add_element(e, a, 3, 1)

    # Print node displacement
    struct.print()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
