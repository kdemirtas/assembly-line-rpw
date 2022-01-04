from assembly_line_rpw.initializer import Initializer
from assembly_line_rpw.solver import Solver
from assembly_line_rpw.preprocessor import PreProcessor


def main():
    filename = "example1.json"
    init = Initializer(filename)
    mod = init.create_model()
    sol = Solver(mod)
    solution = sol.solve()


if __name__ == "__main__":
    main()