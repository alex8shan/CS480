# Name: Mingao Shan - ms1723@truman.edu
# Name: Shreeya Rupakheti - ??????????????????????????????????????@truman.edu

# File farmer.py
# Implements the Farmer problem for state space search

from enum import Enum
from search import *


class Farmer(ProblemState):
    """
    Each state in the Missionaries and Cannibals problem is characterized by
    four pieces of information:
    - Whether the wolf is on the Point A
    - Whether the goal is on the Point A
    - Whether the grain is on the Point A
    - Position of the wagon
    """

    # Total numbers of missionaries and cannibals
    GROUP_SIZE = 3

    class BoatPosition(Enum):
        """Possible positions of the boat"""
        LEFT = 0
        RIGHT = 1

    def __init__(self, num_missionaries, num_cannibals, boat_position):
        self.num_missionaries = num_missionaries
        self.num_cannibals = num_cannibals
        self.boat_position = boat_position

    def __str__(self):
        """Returns a string representation of the state"""
        return "%d %d %s" % (self.num_missionaries,
                             self.num_cannibals,
                             self.boat_position.name)

    def illegal(self):
        """Tests whether the state is illegal"""

        # if position is valid : < 0 or > 1

        # Check that numbers of missionaries and cannibals are valid
        if not (0 <= self.num_missionaries <= self.GROUP_SIZE
                and 0 <= self.num_cannibals <= self.GROUP_SIZE):
            return True

        # Check that no group of missionaries in one place is outnumbered by
        # the cannibals in that place
        return ((0 < self.num_missionaries < self.num_cannibals)
                or (0 < self.GROUP_SIZE - self.num_missionaries
                    < self.GROUP_SIZE - self.num_cannibals))

    # METHODS: move wolf, 

    def equals(self, state):
        """
        Determines whether the state instance and the given state are equal
        """
        return (self.num_missionaries == state.num_missionaries
                and self.num_cannibals == state.num_cannibals
                and self.boat_position == state.boat_position)

    # Each operator corresponds to ferrying a group of people from the current
    # bank to the other bank. This induces a decrease on the numbers of
    # missionaries and cannibals on current bank.
    OPERATORS = [[1, 0], [2, 0], [0, 1], [0, 2], [1, 1]]

    def operatorNames(self):
        """
        Returns a list of operator names in the same order as the applyOperators
        method
        """
        names = []
        for operator in self.OPERATORS:
            names.append('Move %d missionaries and %d cannibals from %s bank'
                         % (operator[0], operator[1], self.boat_position.name))
        return names

    def applyOperators(self):
        """
        Returns a list of possible successors to the current state, some of
        which maybe illegal
        """
        next_states = []

        for operator in self.OPERATORS:
            if self.boat_position == self.BoatPosition.LEFT:
                next_states.append(Farmer(
                    self.num_missionaries - operator[0],
                    self.num_cannibals - operator[1],
                    self.BoatPosition.RIGHT))
            else:
                next_states.append(Farmer(
                    self.num_missionaries + operator[0],
                    self.num_cannibals + operator[1],
                    self.BoatPosition.LEFT))

        return next_states


initialState = Farmer(Farmer.GROUP_SIZE,
                               Farmer.GROUP_SIZE,
                               Farmer.BoatPosition.LEFT)

goalState = Farmer(0, 0, Farmer.BoatPosition.RIGHT)

Search(initialState, goalState)
