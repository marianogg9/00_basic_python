# Write a program printing who won to the roll of dice game
from typing import List

bowling_game_report = [
    ["Leon", [1, 4, 2, 4, 2, 5, 6, 6, 6]],
    ["Marty", [1, 4, 6, 4, 2, 5, 6, 6, 6]],
    ["Anna", [1, 1, 3, 4, 1, 5, 3, 3, 4]],
    ["Mary", [1, 4, 2, 2, 2, 1, 2, 3, 3]]
]


def exercise_4(bowling_game_report: List[str, List]) -> str:
    return


assert exercise_4(bowling_game_report) == "Marty won the game with a score of 40 points"
