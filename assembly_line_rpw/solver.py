from collections import OrderedDict
from assembly_line_rpw.model import Station


class Solution:
    def __init__(self):
        self.stations = []
        self.n_stations = 0

    def add_station(self, station):
        self.stations.append(station)


class Solver:
    def __init__(self, model):
        self.model = model
        self.solution = Solution()

    def solve(self):
        CYCLE_TIME = self.model.settings["CYCLE_TIME"]
        # Find all the successors and compute the rpw values for every task
        for task in self.model.task_dict.values():
            task.find_all_successors(self.model.task_dict)
            task.compute_rpw(self.model.task_dict)

        # Sort tasks by rpw values in descending order
        task_dict_sorted = OrderedDict(sorted(self.model.task_dict.items(), key=lambda x: x[1].rpw, reverse=True))
        task_dict_assigned = {task_id: task.is_assigned() for task_id, task in task_dict_sorted.items()}

        # Assign tasks to stations
        s = 1

        # Create first station if there are no stations
        if not self.solution.stations:
            station = Station(s)
            self.solution.add_station(station)
            s = s + 1

        while not all(list((task_dict_assigned.values()))):
            for task_id, task in task_dict_sorted.items():
                if not task.is_assigned():
                    task_duration = task.duration
                    if (station.station_time + task_duration <= CYCLE_TIME) and self._check_preds(task, task_dict_sorted):
                        station.add_task(task)
                        task.assign_to_station(station.station_id)
                        task_dict_assigned[task_id] = True                       
                    else:
                        if station.station_time < CYCLE_TIME:
                            continue
            if not all(list((task_dict_assigned.values()))):
                station = Station(s)
                self.solution.add_station(station)
                s = s + 1
            

    def _check_preds(self, task, task_dict_sorted):
        check_list = []
        for pred in task.pred_list:
            check_list.append(task_dict_sorted[pred].is_assigned())
        return all(check_list)

        return self.solution



    def print_solution(self):
        if not self.solution:
            print("Solution is empty. Make sure you solved the model first.")
        else:
            # Pretty print the solution to console
            pass

    def solution_to_text(self):
        pass

    