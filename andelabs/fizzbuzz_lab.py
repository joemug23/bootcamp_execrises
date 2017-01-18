def fizz_buzz(num):
    # return fizz, buzz, fizzbuzz or the number itself depending on conditions
    if num % 3 == 0 and num % 5 != 0:
        return 'Fizz'
    elif num % 3 != 0 and num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    else:
        return num
