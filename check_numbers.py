def is_positive(num):
    if int(num) > 0:
        return True
    else:
        return False


def is_negative(num):
    if int(num) < 0:
        return True
    else:
        return False


def is_zero(num):
    if int(num) == 0:
        return True
    else:
        return False


def is_odd(num):
    if int(num) <= 0:
        return False
    if int(num) % 2 != 0:
        return True
    else:
        return False


def is_even(num):
    if int(num) <= 0:
        return False
    if int(num) % 2 == 0:
        return True
    else:
        return False


def is_prime(num):
    if int(num) == 0 or int(num) == 1:
        return False
    result = 0
    total = 0
    while True:
        if total == int(num):
            break
        total += 1
        if int(num) % total == 0:
            result += 1
    if result <= 2:
        return True
    else:
        return False
