def exchange_money(budget,exchange_rate):
    exchanged_money = budget/exchange_rate
    return (exchanged_money)
def get_change(budget,exchanging_value):
    change = budget-exchanging_value
    return (change)
def get_value_of_bills(denomination,number_of_bills):
    total_amount = denomination*number_of_bills
    return (total_amount)
def get_number_of_bills(amount,denomination):
    no_of_bills = amount//denomination
    return (no_of_bills)
def get_leftover_of_bills(amount, denomination):
    no_of_bills = amount//denomination
    amo = no_of_bills*denomination
    left = amount-amo
    return (left)
def exchangeable_value(budget,exchange_rate,spread,denomination):
    t_ex = exchange_rate+exchange_rate*(spread/100)
    t_m = budget/t_ex
    bills = t_m//denomination
    exchanged_money = denomination*bills
    return exchanged_money