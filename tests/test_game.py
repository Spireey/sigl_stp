import os
from pathlib import Path
import sys
import unittest

os.environ["SDL_VIDEODRIVER"] = "dummy"
sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from game import Game


class GameTests(unittest.TestCase):
    def test_game_updates_and_renders_one_frame(self) -> None:
        game = Game()
        try:
            self.assertTrue(game.running)
            game.update()
            game.render()
        finally:
            game.shutdown()
