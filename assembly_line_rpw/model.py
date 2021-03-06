class Task:
    def __init__(self, id, duration, pred_list):
        self.id = id
        self.station_id = None
        self.duration = duration
        self.pred_list = pred_list
        self.succ_list = []
        self.all_succ_list = []
        self.rpw = None
        self.assigned = False
        print(self.id, self.duration, self.pred_list)

    def add_successor(self, succ):
        self.succ_list.append(succ)

    def compute_rpw(self, task_dict):
        self.rpw = self.duration
        for succ_task in self.all_succ_list:
            succ_task_duration = task_dict[succ_task].duration
            self.rpw += succ_task_duration

    def find_all_successors(self, task_dict, task=None):       
        if not task:
            task = self
        for succ in task.succ_list:
            if succ:
                if not succ in self.all_succ_list:
                    self.all_succ_list.append(succ)
                    self.find_all_successors(task_dict, task_dict[succ])

    def assign_to_station(self, station_id):
        self.station_id = station_id
        self.assigned = True

    def is_assigned(self):
        return self.assigned
                
                
class Station:
    def __init__(self, station_id):
        self.station_id = station_id
        self.tasks = []
        self.tasks_list = []
        self.station_time = 0

    def assigned_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)
        self.tasks_list.append(task.id)
        self.station_time += task.duration

class Model:
    def __init__(self, settings, tasks, task_dict):
        self.tasks = tasks
        self.task_dict = task_dict
        self.settings = settings