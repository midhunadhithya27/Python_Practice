"""Functions to help play and score a game of blackjack."""
def value_of_card(card):
    """Determine the scoring value of a card."""
    if card.strip().upper()=='A':
        return 1
    elif card.strip().isdecimal():
        return int(card.strip())
    elif card.strip().upper() in ["K","Q","J"]:
        return 10
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    if value_of_card(card_one)>value_of_card(card_two):
        return card_one
    elif value_of_card(card_one)<value_of_card(card_two):
        return card_two
    elif value_of_card(card_one)==value_of_card(card_two):
        return card_one, card_two
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""
    if card_one.upper()=="A" or card_two.upper()=="A":
        return 1
    if value_of_card(card_one)+value_of_card(card_two) <= 10:
        return 11
    else:
        return 1
def is_blackjack(card_one, card_two):
    """Drmine if the hand is a 'natural' or 'blackjack'."""
    if (card_one.strip().upper() == "A" and value_of_card(card_two) == 10):
        return True
    elif (card_two.strip().upper() == "A" and value_of_card(card_one) == 10):
        return True
    else:
        return False
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    if value_of_card(card_one)==value_of_card(card_two):
        return True
    else:
        return False
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    if value_of_card(card_one)+value_of_card(card_two) in [9,10,11]:
        return True
    else:
        return False