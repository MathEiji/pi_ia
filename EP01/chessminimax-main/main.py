# Matheus Eiji Moriya dos Santos
from chess_minimax import Bot
import random
import time

game = Bot()

print("\nChess Game Started!\n")
print("\nP = PAWN\nR = ROOK\nB = BISHOP\nN = KNIGHT\nQ = QUEEN\n")
print(game.board,"\n")

while not game.board.is_game_over(claim_draw=False):
    time.sleep(2) # Timer so you can know what happened

    if game.board.turn:
        play = game.select_play()
        game.board.push(play)
        print("Challenger plays ", play, "\n")
        print(game.board,"\n")
    else:
        # Random play for testing purposes
        p_play = random.choice([play for play in game.board.legal_moves])
        game.board.push(p_play)
        print("Player plays ", play, "\n")
        print(game.board,"\n")

# Check winner
if game.board.is_checkmate():
    if game.board.turn:
        print("Congrats, you won!")
    else:
        print("My regards, you lost....")

# Check if its a draw
if game.board.is_stalemate():
    print("Its a Draw by stalemate!")
if game.board.is_insufficient_material():
    print("Its a Draw by insufficient pieces!")

print(game.board.outcome())