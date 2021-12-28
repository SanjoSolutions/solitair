from create_solvable_solitair_game import create_solvable_solitair_game
# from Solitair import Solitair
from SolitairSolver import SolitairSolver

def main():
    solitair = create_solvable_solitair_game()
    # solitair = Solitair.create()
    solver = SolitairSolver()
    solution = solver.solve(solitair)
    print(solution)

if __name__ == '__main__':
    main()
