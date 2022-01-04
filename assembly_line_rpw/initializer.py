import os
import json
from assembly_line_rpw import parser

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

        m = model.Model(settings, tasks, task_dict)
        return model

