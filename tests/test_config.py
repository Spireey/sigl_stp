from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

import config


class ConfigTests(unittest.TestCase):
    def test_window_configuration_has_valid_values(self) -> None:
        self.assertIsInstance(config.WINDOW_TITLE, str)
        self.assertGreater(config.WINDOW_SIZE[0], 0)
        self.assertGreater(config.WINDOW_SIZE[1], 0)
        self.assertGreater(config.FPS, 0)
        self.assertEqual(len(config.BACKGROUND_COLOR), 3)
