class Solution:
    def __init__(self):
        pass

class Solver:
    def __init__(self, model):
        self.model = model
        self.solution = {}

    def solve(self):
        # Write the solver code here

        for task in self.model.task_dict.values():
            task.find_all_successors(self.model.task_dict)

        return self.solution


    def print_solution(self):
        if not self.solution:
            print("Solution is empty. Make sure you solved the model first.")
        else:
            # Pretty print the solution to console
            pass

    def solution_to_text(self):
        pass

    