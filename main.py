from assembly_line_rpw.initializer import Initializer
from assembly_line_rpw.solver import Solver


def main():
    filename = "example1.json"
    model = Initializer(filename)
    sol = Solver(model)
    solution = sol.solve()


if __name__ == "__main__":
    main()