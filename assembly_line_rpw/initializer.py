import os
import json
from assembly_line_rpw import parser
from assembly_line_rpw import model
from assembly_line_rpw.model import Task


class DirectoryStructure:
    def __init__(self):
        self.root_dir = os.path.dirname(os.path.dirname(__file__))
        self.test_dir = os.path.join(self.root_dir, "tests")
        self.docs_dir = os.path.join(self.root_dir, "docs")
        self.files_dir = os.path.join(self.root_dir, "files")


class Initializer:
    def __init__(self, filename):
        # Get to the absolute path of the file given the filename
        ds = DirectoryStructure()
        file_path = os.path.join(ds.files_dir, filename)
        with open(file_path) as fp:
            self.input = json.load(fp)

    def create_model(self):
        p = parser.Parser(self.input)
        parse_result = p.parse()

        task_dict = {}
        for task in parse_result["tasks"]:
            task_id = task["id"]
            duration = task["duration"]
            pred_list = task["preds"]
            t = Task(task_id, duration, pred_list)
            task_dict[task_id] = t

        mod = model.Model(parse_result["settings"], parse_result["tasks"], task_dict)
        return mod

