from socha.api.networking.player_client import IClientHandler
from socha.api.plugin.penguins import *
from socha.starter import Starter

class Logic(IClientHandler):
    gameState: GameState

    def calculate_move(self) -> Move:
        possibleMoves = self.gameState.possible_moves
        return possibleMoves[0]

    def on_update(self, state: GameState):
        self.gameState = state
        
    def on_error(self, logMessage: str):
        ...
        
if __name__ == "__main__":
    Starter(Logic())