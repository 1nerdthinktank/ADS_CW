# Analysis of Algorithm (Big-O performance)

# Now, your task is to measure the running time of your solution with 5 different sequence length (maybe 2k, 10k,
# 50k, 200k, 1000k) and plot the graph. What is the big O performance of the code?l

# Sieve of Eratosthenes

# Principle is that for a number to be non-prime, it must have a number smaller than it that
# multiplies by another number to produce it. Therefore, by starting with those smaller numbers,
# and eliminating the number which they produce by multiplication, after running through all number
# smaller than n you can be left with primes

class PrimesToNth:

    def __init__(self, n: int) -> None:
        self.n = n

    def eratosthenes_sieve(self) -> list[float]:
        # assign boolean "grid" set to true
        grid = [True for _ in range(self.n + 1)]
        # start from 2 as 0 and 1 are not primes
        i = 2
        # up to the square root of n (minimum range needed to check all squares on grid)
        while i < (self.n ** 0.5) + 1:
            # start from end of last iteration multiple, stop: n+1, step: i (current number)
            for j in range(i ** 2, self.n + 1, i):
                # set to not prime
                grid[j] = False
            i += 1
            # list comprehension, using index value from enumerate as value (higher than 2)
        return [i for i, is_prime_num in enumerate(grid) if is_prime_num and i >= 2]

    def all_primes_to_nth(self) -> list[int]:

        prime_list = []

        def is_prime(x) -> bool:
            if x < 2:
                return False
            for i in range(2, x):
                if x % i == 0:
                    return False
            else:
                return True

        for y in range(2, self.n + 1):
            if is_prime(y):
                prime_list.append(y)

        return prime_list

    def prime_generator(self) -> list[int]:
        for n in range(2, self.n):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                yield n

    def create_primes(self):

        prime_list = []

        def is_prime(x) -> bool:
            if x < 2:
                return False
            for i in range(2, x):
                if x % i == 0:
                    return False
            else:
                return True

        for y in range(2, self.n + 1):
            if is_prime(y):
                prime_list.append(y)

        return prime_list


if __name__ == "__main__":

    # Test

    alix_algo = PrimesToNth(10)
    elifsu_algo = PrimesToNth(10)
    arda_algo = PrimesToNth(10)
    victoria_algo = PrimesToNth(10)

    print(f"{alix_algo.eratosthenes_sieve()}\n"
          f"{elifsu_algo.all_primes_to_nth()}\n"
          f"{list(arda_algo.prime_generator())}\n"
          f"{victoria_algo.create_primes()}")

    # End
