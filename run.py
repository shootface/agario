import os,sys
workingPath = os.getcwd()
sys.path.append(os.path.join(workingPath, "src"))
from src.game import Game

if __name__ == "__main__":
    Game.getGame()
