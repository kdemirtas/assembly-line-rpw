

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
            raise UserWarning("Caution required by user. Tasks are not provided")

        return tasks

    def parse(self):
        settings = self._parse_settings()
        tasks = self._parse_tasks()

        parse_result = {
            "settings": settings,
            "tasks": tasks,
        }

        return parse_result
