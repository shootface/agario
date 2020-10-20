from __future__ import annotations
from abc import ABC, abstractmethod

class GameElement(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def enemyDetection(self,player_list):
        pass
