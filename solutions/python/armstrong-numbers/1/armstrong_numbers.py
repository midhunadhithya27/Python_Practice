def is_armstrong_number(number):
    s = str(number)
    c = 0
    for i in s:
        c += 1
    sum = 0 
    for i in s:
        n = int(i)
        sum += n**c
    if (sum==number):
        return True
    else:
        return False

