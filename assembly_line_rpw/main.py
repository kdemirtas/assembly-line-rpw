from assembly_line_rpw import initializer, solver


def main():
    filename = "example1.json"
    model = initializer.Initializer(filename)
    s = solver.Solver(model)
    solution = s.solve()


if __name__ == __main__:
    main()