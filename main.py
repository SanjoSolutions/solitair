from create_solvable_solitaire_game import create_solvable_solitaire_game
# from Solitaire import Solitaire
from SolitaireSolver import SolitaireSolver

def main():
    solitair = create_solvable_solitaire_game()
    # solitair = Solitaire.create()
    solver = SolitaireSolver()
    solution = solver.solve(solitair)
    print(solution)

if __name__ == '__main__':
    main()
