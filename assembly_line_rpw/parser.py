

class Parser:
    def __init__(self, input):
        self.input = input

    def _parse_settings(self):
        settings = self.input.get("settings")
        if settings is None:
            raise UserWarning("Caution required by user. No settings provided")

        return settings

    def _parse_tasks(self):
        tasks = self.input.get("tasks")
        if tasks is None:
            raise UserWarning("Caution required by user. Nodes are not provided")

        task_dict = {}
        for task in tasks:
            task_id = task["id"]
            duration = task["duration"]
            pred_list = task["pred_list"]
            t = data.model.task(task_id, duration, pred_list)
            task_dict[t.node_id] = t

        return tasks, task_dict

    def parse(self):
        settings = self._parse_settings()
        tasks, task_dict = self._parse_tasks()

        parse_result = {
            "settings": settings,
            "tasks": tasks,
            "task_dict": task_dict
        }

        return result
