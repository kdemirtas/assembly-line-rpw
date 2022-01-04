class Task:
    def __init__(self, id, duration, pred_list):
        self.id = id
        self.duration = duration
        self.pred_list = pred_list
        self.succ_list = []
        self.all_succ_list = []
        self.rpw = None
        print(self.id, self.duration, self.pred_list)

    def add_successor(self, succ):
        self.succ_list.append(succ)

    def compute_rpw(self):
        pass

    def _find_all_successors(self, task_dict, succ_task=None):       
        if not succ_task:
            succ_task = self
        for succ in succ_task.succ_list:
            if succ:
                if not succ in self.all_succ_list:
                    self.all_succ_list.append(succ)
                    self._find_all_successors(task_dict, task_dict[succ])
                
                
class Station:
    def __init__(self):
        self.tasks = []

    def assigned_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)

class Model:
    def __init__(self, settings, tasks, task_dict):
        self.tasks = tasks
        self.task_dict = task_dict
        self.settings = settings
        self.stations = []