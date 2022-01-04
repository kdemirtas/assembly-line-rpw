class Task:
    def __init__(self, id, duration, pred):
        self.id = id
        self.duration = duration
        self.pred = pred

    def _compute_rpw(self):
        pass

class Station:
    def __init__(self):
        self.tasks = []

    def assigned_tasks(self):
        return self.tasks

    def add_task(self, task):
        self.tasks.append(task)