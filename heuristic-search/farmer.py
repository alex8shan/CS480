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
    - Position of the wolf
    - Position of the goat
    - Position of the grain
    - Position of the farmer
    """

    # Total numbers of missionaries and cannibals
    GROUP_SIZE = 3

    class FarmerPosition(Enum):
        """Possible positions of the farmer"""
        POINTA = 0
        POINTB = 1

    class WolfPosition(Enum):
        """Possible positions of the wolf"""
        POINTA = 0
        POINTB = 1

    class GoatPosition(Enum):
        """Possible positions of the goat"""
        POINTA = 0
        POINTB = 1
    
    class GrainPosition(Enum):
        """Possible positions of the grain"""
        POINTA = 0
        POINTB = 1
    
    def __init__(self, wolf_position, goat_position, grain_position, farmer_position):
        self.wolf_position = wolf_position
        self.goat_position = goat_position
        self.grain_position = grain_position
        self.farmer_position = farmer_position

    def __str__(self):
        """Returns a string representation of the state"""
        return "%s %s %s %s" % (self.wolf_position.name,
                                self.goat_position.name,
                                self.grain_position.name,
                                self.farmer_position.name)

    def illegal(self):
        """Tests whether the state is illegal"""

        # if position is valid : < 0 or > 1

        # Check that numbers of missionaries and cannibals are valid
        # if not (0 <= self.num_missionaries <= self.GROUP_SIZE
        #         and 0 <= self.num_cannibals <= self.GROUP_SIZE):
        #     return True

        # Check that no group of missionaries in one place is outnumbered by
        # the cannibals in that place
        # return ((0 < self.num_missionaries < self.num_cannibals)
        #         or (0 < self.GROUP_SIZE - self.num_missionaries
        #             < self.GROUP_SIZE - self.num_cannibals))

    # METHODS: move wolf, 

    def equals(self, state):
        """
        Determines whether the state instance and the given state are equal
        """
        # return (self.num_missionaries == state.num_missionaries
        #         and self.num_cannibals == state.num_cannibals
        #         and self.farmer_position == state.farmer_position)

    # Each operator corresponds to ferrying a group of people from the current
    # bank to the other bank. This induces a decrease on the numbers of
    # missionaries and cannibals on current bank.
    # OPERATORS = [[1, 0], [2, 0], [0, 1], [0, 2], [1, 1]]

    def operatorNames(self):
        """
        Returns a list of operator names in the same order as the applyOperators
        method
        """
        # names = []
        # for operator in self.OPERATORS:
        #     names.append('Move %d missionaries and %d cannibals from %s bank'
        #                  % (operator[0], operator[1], self.farmer_position.name))
        # return names

    def applyOperators(self):
        """
        Returns a list of possible successors to the current state, some of
        which maybe illegal
        """
        # next_states = []

        # for operator in self.OPERATORS:
        #     if self.farmer_position == self.FarmerPosition.LEFT:
        #         next_states.append(Farmer(
        #             self.num_missionaries - operator[0],
        #             self.num_cannibals - operator[1],
        #             self.FarmerPosition.RIGHT))
        #     else:
        #         next_states.append(Farmer(
        #             self.num_missionaries + operator[0],
        #             self.num_cannibals + operator[1],
        #             self.FarmerPosition.LEFT))

        # return next_states


initialState = Farmer(Farmer.WolfPosition.POINTA,
                        Farmer.GoatPosition.POINTA,
                        Farmer.GrainPosition.POINTA,
                        Farmer.FarmerPosition.POINTA)

goalState = Farmer(Farmer.WolfPosition.POINTB,
                        Farmer.GoatPosition.POINTB,    
                        Farmer.GrainPosition.POINTB,
                        Farmer.FarmerPosition.POINTB)

Search(initialState, goalState)
