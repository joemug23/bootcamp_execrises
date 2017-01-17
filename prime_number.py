
def prime_numbers(n):
    # generate a list of prime number from 0 to next
    if isinstance(n, str):
        raise TypeError
    elif isinstance(n, float):
        raise TypeError
    elif isinstance(n, list):
        raise TypeError
    elif isinstance(n, dict):
        raise TypeError
    else:
        is_prime = []
        if n < 0:
            raise ValueError
        elif n == 0:
            return is_prime
        elif n == 1:
            return "That is a special case"

        for num in range(n):
            if num > 1:
                for factor in range(2, num):
                    if num % factor == 0:
                        break
                else:
                    is_prime.append(num)
    return is_prime
