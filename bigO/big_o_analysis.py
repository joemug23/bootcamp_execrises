
import big_o

from prime_number import prime_numbers

positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
best, others = big_o.big_o(prime_numbers, positive_int_generator, n_repeats=100)
print(best)