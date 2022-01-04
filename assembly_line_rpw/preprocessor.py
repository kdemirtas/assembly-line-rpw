class PreProcessor:
    def __init__(self, model):
        self.model = model
        self.task_dict = model.task_dict
        self.tasks = model.tasks

    def _find_immediate_successors(self):
        for task in self.tasks:
            for pred in task.pred_list:
                pred_task = self.task_dict[pred]
                pred_task.add_successor(task)