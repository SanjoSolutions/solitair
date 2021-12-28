import math


class Solver:
    def solve(self, game):
        state = game

        bound = self.heuristic_function(state)

        while True:
            solution, next_bound = self.search(state, bound)

            if solution is not None:
                return solution
            else:
                bound = next_bound

    def search(self, state, bound):
        estimated_total_cost = self.estimate_total_distance(state)
        if estimated_total_cost > bound:
            return None, estimated_total_cost
        if self.is_solution(state):
            return state, None
        minimum_estimated_total_cost = math.inf
        possible_moves = self.determine_possible_moves(state)
        for move in possible_moves:
            next_state = self.do_move(state, move)
            solution, estimated_total_cost_of_next_state = self.search(next_state, bound)
            if solution is not None:
                return solution, None
            elif estimated_total_cost_of_next_state < minimum_estimated_total_cost:
                minimum_estimated_total_cost = estimated_total_cost_of_next_state
        return None, minimum_estimated_total_cost

    def is_solution(self, state):
        raise NotImplementedError()

    def estimate_total_distance(self, state):
        return self.traveled_distance(state) + self.heuristic_function(state)

    def traveled_distance(self):
        raise NotImplementedError()

    def heuristic_function(self):
        raise NotImplementedError()

    def do_move(self, state, move):
        raise NotImplementedError()
