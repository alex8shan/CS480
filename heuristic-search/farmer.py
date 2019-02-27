# Name: Shreeya Rupakheti - sr7172@truman.edu
# Name: Minghao Shan - ms1723@truman.edu

# File farmer.py
# Implements the Farmer Problem

from search import *

class FarmerState(ProblemState):
    """
    1 represent presence of wolf or goat or grain in point A or point B and
    0 represent absence.
    The first three 111 represents wolfA, goatA and grain respectively such
    that two adjacent 11 in both point A or B will be illegal state.
    """

    def __init__(self, wolfA, goatA, grainA, famer, wolfB, goatB, grainB):
        self.wolfA = wolfA
        self.goatA = goatA
        self.grainA = grainA
        self.famer = famer
        self.wolfB = wolfB
        self.goatB = goatB
        self.grainB = grainB


    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "A: " + str(self.wolfA) + str(self.goatA) + str(self.grainA) \
            + " (Next move will be from point " + str(self.famer) + ") " + " B: " \
            + str(self.wolfB) + str(self.goatB) + str(self.grainB)


    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        if self.wolfA < 0 or self.goatA < 0 or self.grainA < 0:
            return 1
        if self.wolfA > 1 or self.goatA > 1 or self.grainA > 1:
            return 1
        if self.wolfA == 1 and self.goatA == 1 and self.famer == 'B':
            return 1
        if self.goatA == 1 and self.grainA == 1 and self.famer == 'B':
            return 1
        if self.wolfB == 1 and self.goatB == 1 and self.famer == 'A':
            return 1
        if self.goatB == 1 and self.grainB == 1 and self.famer == 'A':
            return 1
        if self.wolfB != 1 and self.goatB != 1 and self.grainB != 1 and self.famer != 'B':
            return 1
        return 0


    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.wolfA == state.wolfA and self.goatA == state.goatA and \
            self.grainA == state.grainA and self.famer == state.famer and \
            self.wolfB == state.wolfB and self.goatB == state.goatB and \
            self.grainB == state.grainB

    # move goatA to point B


    def moveGoat(self):
        if self.famer == 'A' and self.goatA == 1:
            return FarmerState(self.wolfA, self.goatA - 1, self.grainA, 'B',
                        self.wolfB, self.goatB + 1, self.grainB)
        else:
            return FarmerState(self.wolfA, self.goatA + 1, self.grainA, 'A',
                        self.wolfB, self.goatB - 1, self.grainB)

    # move wolfA to point B


    def moveWolf(self):
        if self.famer == 'A' and self.wolfA == 1:
            return FarmerState(self.wolfA - 1, self.goatA, self.grainA, 'B',
                        self.wolfB + 1, self.goatB, self.grainB)
        else:
            return FarmerState(self.wolfA + 1, self.goatA, self.grainA, 'A',
                        self.wolfB - 1, self.goatB, self.grainB)

    # move grain to point B


    def moveGrain(self):
        if self.famer == 'A' and self.grainA == 1:
            return FarmerState(self.wolfA, self.goatA, self.grainA - 1, 'B',
                        self.wolfB, self.goatB, self.grainB + 1)
        else:
            return FarmerState(self.wolfA, self.goatA, self.grainA + 1, 'A',
                        self.wolfB, self.goatB, self.grainB - 1)

        # move wolfA or goatA to point B


    def moveWolfOrGoat(self):
        if self.famer == 'A' and self.wolfA == 1 and self.goatA == 0 and self.grainA == 1:
            return FarmerState(self.wolfA - 1, self.goatA - 1, self.grainA, 'B',
                        self.wolfB + 1, self.goatB + 1, self.grainB)
        else:
            return FarmerState(self.wolfA, self.goatA - 1, self.grainA, 'A',
                        self.wolfB, self.goatB + 1, self.grainB)

        # move wolfA or grain to point B


    def moveWolfOrGrain(self):
        if self.famer == 'A' and self.wolfA == 0 and self.goatA == 1 and self.grainA == 1:
            return FarmerState(self.wolfA - 1, self.goatA, self.grainA - 1, 'B',
                        self.wolfB + 1, self.goatB, self.grainB + 1)
        else:
            return FarmerState(self.wolfA - 1, self.goatA, self.grainA, 'A',
                        self.wolfB + 1, self.goatB, self.grainB)


    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["moveGoat", "moveWolf", "moveGrain",
            "moveWolfOrGoat", "moveWolfOrGrain"]


    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.moveGoat(), self.moveWolf(), self.moveGrain(),
            self.moveWolfOrGoat(), self.moveWolfOrGrain()]

Search(FarmerState(1, 1, 1, 'A', 0, 0, 0), FarmerState(0, 0, 0, 'B', 1, 1, 1))
