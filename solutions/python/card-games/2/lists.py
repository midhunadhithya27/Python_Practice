"""Functions for tracking poker hands and assorted card tasks."""

def get_rounds(number):
    lists = [number,number+1,number+2]
    return lists
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2
def list_contains_round(rounds, number):
    return number in rounds
def card_average(hand):
    return sum(hand)/len(hand)
def approx_average_is_average(hand):
    avg = sum(hand)/len(hand)
    middle_index = len(hand)//2
    median = hand[middle_index]
    average = (hand[0]+hand[-1])/2
    return avg==average or avg == median
def average_even_is_average_odd(hand):
    sum_odd = sum(hand[::2])
    no = len(hand[::2])
    sum_even = sum(hand[1::2])
    ne = len(hand[1::2])
    avg_odd = sum_odd/no
    avg_even = sum_even/ne
    if avg_even==avg_odd:
        return True
    else:
        return False
def maybe_double_last(hand):
    if hand[-1]==11:
        return hand[:-1]+[22,]
    else:
        return hand
    