from Solver import Solver
from dataclasses import dataclass, field
from typing import Any
from Suit import Suit
from MoveToOtherPile import MoveToOtherPile
from MoveToFoundationPile import MoveToFoundationPile
from DrawMove import DrawMove
from MoveFromStockPileToPile import MoveFromStockPileToPile
from MoveFromStockPileToFoundationPile import MoveFromStockPileToFoundationPile
from Rank import Rank
from Facing import Facing
from heapq import heappush, heappop

MAXIMUM_NUMBER_OF_MOVES = 512

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


class SolitairSolver(Solver):
    def solve(self, game):
        state = game

        open_set = []
        prioritized_item = PrioritizedItem(
            self.estimate_total_distance(state),
            state
        )
        heappush(open_set, prioritized_item)

        amount_of_moves = 0
        while len(open_set) >= 1:
            prioritized_item2 = heappop(open_set)
            state = prioritized_item2.item
            if len(state.moves) < MAXIMUM_NUMBER_OF_MOVES:
                possible_moves = self.determine_possible_moves(state)
                for move in possible_moves:
                    next_state = do_move(state, move)

                    if self.is_solution(next_state):
                        return next_state

                    prioritized_item = PrioritizedItem(
                        self.estimate_total_distance(next_state),
                        next_state
                    )
                    heappush(open_set, prioritized_item)
        return None

    def is_solution(self, state):
        return self.heuristic_function(state) == 0

    def estimate_total_distance(self, state):
        return self.traveled_distance(state) + self.heuristic_function(state)

    def traveled_distance(self, state):
        return len(state.moves)

    def heuristic_function(self, state):
        return (
            sum(len(pile) for pile in state.piles) +
            len(state.stock_pile) +
            2 * len(state.deck)
        )

    def determine_possible_moves(self, state):
        moves = []
        for pile_index in range(len(state.piles)):
            pile = state.piles[pile_index]

            if len(pile) >= 1:
                card = pile[-1]
                foundation_pile_index = card.suit.value
                foundation_pile = state.foundation_piles[foundation_pile_index]
                if self.can_card_be_put_on_foundation_pile(card, foundation_pile):
                    move = MoveToFoundationPile(
                        pile_index,
                        foundation_pile_index
                    )
                    moves.append(move)

                for card_index in range(len(pile) - 1, -1, -1):
                    cards = pile[card_index:]
                    if card.facing == Facing.UP and self.is_group(cards):
                        group = cards
                        for to_pile_index in range(len(state.piles)):
                            to_pile = state.piles[to_pile_index]
                            card = group[0]
                            if (
                                to_pile_index != pile_index and
                                self.can_card_be_put_on_pile(card, to_pile)
                            ):
                                move = MoveToOtherPile(
                                    pile_index,
                                    card_index,
                                    to_pile_index
                                )
                                moves.append(move)
                    else:
                        break

        if len(state.stock_pile) >= 1:
            card = state.stock_pile[-1]
            for pile_index in range(len(state.piles)):
                pile = state.piles[pile_index]
                if self.can_card_be_put_on_pile(card, pile):
                    move = MoveFromStockPileToPile(pile_index)
                    moves.append(move)

            foundation_pile_index = card.suit.value
            foundation_pile = state.foundation_piles[foundation_pile_index]
            if self.can_card_be_put_on_foundation_pile(card, foundation_pile):
                move = MoveFromStockPileToFoundationPile(foundation_pile_index)
                moves.append(move)

        move = DrawMove()
        moves.append(move)

        return moves

    def can_card_be_put_on_pile(self, card, pile):
        return (
            (len(pile) == 0 and card.rank == Rank.KING) or
            (len(pile) >= 1 and self.do_cards_connect(pile[-1], card))
        )

    def can_card_be_put_on_foundation_pile(self, card, foundation_pile):
        return (
            (len(foundation_pile) == 0 and card.rank == Rank.ACE) or
            (
                len(foundation_pile) >= 1 and
                self.do_cards_stack_on_foundation_pile(
                    foundation_pile[-1],
                    card
                )
            )
        )

    def is_group(self, cards):
        for card_index in range(1, len(cards)):
            previous_card = cards[card_index - 1]
            card = cards[card_index]
            if not self.do_cards_connect(previous_card, card):
                return False
        return True

    def do_cards_connect(self, card_a, card_b):
        return (
            card_a.rank - card_b.rank == 1 and
            (
                (card_a.is_black() and card_b.is_red()) or
                (card_a.is_red() and card_b.is_black())
            )
        )

    def do_cards_stack_on_foundation_pile(self, card_a, card_b):
        return (
            card_a.suit == card_b.suit and
            (card_b.rank - card_a.rank == 1 or (card_a.rank == Rank.ACE and card_b.rank == Rank.TWO))
        )


def do_move(state, move):
    if isinstance(move, MoveToFoundationPile):
        next_state = do_move_to_foundation_pile(state, move)
    elif isinstance(move, MoveToOtherPile):
        next_state = do_move_to_other_pile(state, move)
    elif isinstance(move, DrawMove):
        next_state = do_draw(state, move)
    elif isinstance(move, MoveFromStockPileToPile):
        next_state = do_move_from_stock_pile_to_pile(state, move)
    elif isinstance(move, MoveFromStockPileToFoundationPile):
        next_state = do_move_from_stock_pile_to_foundation_pile(state, move)
    else:
        raise TypeError('Unexpected type for move: "' + type(move) + '"')
    return next_state


def do_move_to_foundation_pile(state, move: MoveToFoundationPile):
    next_state = state.copy()
    card = next_state.piles[move.from_pile_index].pop()
    next_state.foundation_piles[move.to_foundation_pile_index].append(card)
    next_state.moves.append(move)
    return next_state


def do_move_to_other_pile(state, move: MoveToOtherPile):
    next_state = state.copy()
    group = next_state.piles[move.from_pile_index][move.card_index:]
    next_state.piles[move.from_pile_index] = next_state.piles[move.from_pile_index][:move.card_index]
    next_state.piles[move.to_pile_index].extend(group)
    next_state.moves.append(move)
    return next_state


def do_draw(state, move: DrawMove):
    next_state = state.copy()
    next_state.draw()
    next_state.moves.append(move)
    return next_state


def do_move_from_stock_pile_to_pile(state, move: MoveFromStockPileToPile):
    next_state = state.copy()
    card = next_state.stock_pile.pop()
    next_state.piles[move.pile_index].append(card)
    next_state.moves.append(move)
    return next_state


def do_move_from_stock_pile_to_foundation_pile(state, move: MoveFromStockPileToFoundationPile):
    next_state = state.copy()
    card = next_state.stock_pile.pop()
    next_state.foundation_piles[move.foundation_pile_index].append(card)
    next_state.moves.append(move)
    return next_state
