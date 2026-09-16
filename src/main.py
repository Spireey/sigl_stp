import numpy as np
import torch

from game import Game


def main() -> None:
    print(f"PyTorch version: {torch.__version__}")
    Game().run()


if __name__ == "__main__":
    main()
