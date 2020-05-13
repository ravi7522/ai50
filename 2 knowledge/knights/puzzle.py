from logic import *
import termcolor

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
        #info from the structure of the problem
        Or(AKnight, AKnave),                # A is either a knight or a knave
        Implication(AKnight, Not(AKnave)),  # A can not be a knace if it is a knight
        Implication(AKnave, Not(AKnight)),  
        #information from given statements
        Biconditional(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
        #info from the structure of the problem
        Or(AKnight, AKnave),                # A is either a knight or a knave
        Implication(AKnight, Not(AKnave)),  # A can not be a knace if it is a knight
        Or(BKnight, BKnave),                # B is either a knight or a knave
        Implication(BKnight, Not(BKnave)),  # B can not be a knace if it is a knight
        #information from given statements
        Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
        #info from the structure of the problem
        Or(AKnight, AKnave),                # A is either a knight or a knave
        Implication(AKnight, Not(AKnave)),  # A can not be a knace if it is a knight
        Or(BKnight, BKnave),                # B is either a knight or a knave
        Implication(BKnight, Not(BKnave)),  # B can not be a knace if it is a knight
        #information from the given statements
        Biconditional(AKnight, Or(And(AKnight, BKnight),
                                  And(AKnave, BKnave))),
        Biconditional(BKnight, Or(And(AKnight, BKnave),
                                  And(AKnave, BKnight))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
        #info from the structure of the problem
        Or(AKnight, AKnave),                # A is either a knight or a knave
        Implication(AKnight, Not(AKnave)),  # A can not be a knace if it is a knight
        Or(BKnight, BKnave),                # B is either a knight or a knave
        Implication(BKnight, Not(BKnave)),  # B can not be a knace if it is a knight
        Or(CKnight, CKnave),                # C is either a knight or a knave
        Implication(CKnight, Not(CKnave)),  # C can not be a knace if it is a knight
        #information from the given statements
        Biconditional(Or(AKnight, AKnight), 
                      Or(AKnight, AKnave)),
        Biconditional(BKnight, Biconditional(AKnight, AKnave)),
        Biconditional(BKnight, CKnave),
        Biconditional(CKnight, AKnight)
    
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            termcolor.cprint("    Not yet implemented.", "red")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    termcolor.cprint(f"    {symbol}", "green")


if __name__ == "__main__":
    main()
