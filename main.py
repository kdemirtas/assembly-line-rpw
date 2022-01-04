from assembly_line_rpw.initializer import Initializer
from assembly_line_rpw.solver import Solver
from assembly_line_rpw.preprocessor import PreProcessor


def main():
    filename = "example1.json"
    init = Initializer(filename)
    mod = init.create_model()
    pre = PreProcessor(mod)
    mod = pre.process()
    sol = Solver(mod)
    solution = sol.solve()

    print("Solve complete")


if __name__ == "__main__":
    main()