from pathlib import Path
import unittest


class ProjectFilesTests(unittest.TestCase):
    def test_required_dependencies_are_declared(self) -> None:
        dependencies = (Path(__file__).parents[1] / "requirements.txt").read_text().splitlines()
        self.assertEqual(dependencies, ["torch", "pygame", "numpy"])
