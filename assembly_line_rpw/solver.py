from collections import OrderedDict


class Solution:
    def __init__(self):
        pass

class Solver:
    def __init__(self, model):
        self.model = model
        self.solution = {}

    def solve(self):
        # Find all the successors and compute the rpw values for every task
        for task in self.model.task_dict.values():
            task.find_all_successors(self.model.task_dict)
            task.compute_rpw(self.model.task_dict)

        # Sort tasks by rpw values in descending order
        task_dict_sorted = OrderedDict(sorted(self.model.task_dict.items(), key=lambda x: x[1].rpw, reverse=True))
        return self.solution


    def print_solution(self):
        if not self.solution:
            print("Solution is empty. Make sure you solved the model first.")
        else:
            # Pretty print the solution to console
            pass

    def solution_to_text(self):
        pass

    