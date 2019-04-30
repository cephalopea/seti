# This module covers the decision-making functions and payoff matrices
# of civilizations when they are interacting.
import civilization

strategies = ["attack", "communicate"]

#           A                   C
#   _______________________________________
# A | 1-2 \ 2-1 | 1-2 \ 0                 |
#   |_____________________________________|
# C |0 \ 2-1    | 1+ (1+2/5) \ 2+ (1+2/5) |
#   |_____________________________________|