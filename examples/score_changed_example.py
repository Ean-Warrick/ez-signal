# this example illustrates a situation where a developer wants different functions to run simultaneously
# when a score value is changed.

import ezsignal

score_changed_signal = ezsignal.Signal()


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


#  connect the above functions to score_changed_signal
print_connection = score_changed_signal.connect(print_new_score)
score_above_connection = score_changed_signal.connect(is_new_score_above_ten)
score_divisible_connection = score_changed_signal.connect(is_new_score_divisible_by_3)

thread_bundle = score_changed_signal.emit(9)  # score value is changed to 9 [example]

thread_bundle.join()  # yields thread until all connected functions finish running

# output
# New score: 9
# Score is below 10
# Score is divisible by 3
