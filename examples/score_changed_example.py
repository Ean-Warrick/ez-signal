"""
Example situation: A developer wants different functions to run asynchronously when a score value
inside a ScoreBoard instance is changed.
"""

from ezsignal import Event


class ScoreBoard:
    def __init__(self):
        self._score_changed_event = Event()
        self.score_changed = self._score_changed_event.signal
        self.score = 0

    def add_to_score(self, amount):
        self.score += amount
        self._score_changed_event.emit(self.score)


score_board = ScoreBoard()


def print_new_score(new_score):
    print("New score:", new_score)


def is_new_score_above_ten(new_score):
    if new_score > 10:
        print("Score is above 10")
    else:
        print("Score is below 10")


def is_new_score_divisible_by_3(new_score):
    if new_score % 3 == 0:
        print("Score is divisible by 3")
    else:
        print("Score is not divisible by 3")


print_connection = score_board.score_changed.connect(print_new_score)
above_connection = score_board.score_changed.connect(is_new_score_above_ten)
divisible_connection = score_board.score_changed.connect(is_new_score_divisible_by_3)

score_board.add_to_score(5)
print("-------------------")
score_board.add_to_score(7)

# Output:
""" 
New score: 5
Score is below 10
Score is not divisible by 3
--------------------
New score: 12
Score is above 10
Score is divisible by 3

"""
