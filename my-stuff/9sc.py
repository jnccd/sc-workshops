from socha import *

class Logic(IClientHandler):
    gameState: GameState

    def calculate_move(self) -> Move:
        moves = self.gameState.possible_moves
        
        bestmove = None
        bestscore = -1
        for m in moves:
            future_state: GameState = self.gameState.perform_move(m)
            
            score = 0
            score += future_state.fishes.get_fish_by_team(self.gameState.current_team)
            
            if score > bestscore:
                bestscore = score
                bestmove = m
        
        return bestmove

    def on_update(self, state: GameState):
        self.gameState = state

    def on_error(self, logMessage: str):
        ...


if __name__ == "__main__":
    Starter(Logic(), "localhost", 13050)