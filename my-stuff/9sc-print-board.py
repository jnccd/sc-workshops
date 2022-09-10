from socha import *

class Logic(IClientHandler):
    gameState: GameState

    def calculate_move(self) -> Move:
        possibleMoves = self.gameState.possible_moves

        # Print board
        for y in range(0,8):
            for x in range(0,8):
                f = self.gameState.board.get_field(Coordinate(x,y, False))
                if f.get_fish() is None:
                    print(f.get_team().color()[0], end="")
                else:
                    print(f.get_fish(), end="")
            print("")

        return possibleMoves[0]

    def on_update(self, state: GameState):
        self.gameState = state
        
    def on_error(self, logMessage: str):
        ...
        
if __name__ == "__main__":
    Starter(Logic())