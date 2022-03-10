#
# Algorithm Timing Driver Code
#

import timeit
import random
from matplotlib import pyplot as plt
from InterviewQuestionAlgorithm import PrimesToNth


def float_list_gen(list_size: int) -> list[int]:
    sorted_list = [x for x in range(list_size)]
    float_list = []
    for x in sorted_list:
        float_list.append(float(x))
    random.shuffle(float_list)
    return float_list


if __name__ == "__main__":
    # Timeit Config Setting
    no_of_times = 10

    # Initialise Plot Data
    sum_of_floats_x_axis = []
    alix_list_of_times = []
    arda_list_of_times = []
    elifsu_list_of_times = []
    victoria_list_of_times = []

    # Generate Data Input
    float_list_input = float_list_gen(int(input("\nPlease enter size of data list input: \n")))
    print(f"Input: \n{float_list_input}")

    sum_of_float_list = sum(float_list_input)

    for i in range(5):
        print(f"\nSum of List: {sum_of_float_list}")

        # Construct Algorithm Objects and Input
        alix_algo = PrimesToNth(int(sum_of_float_list))
        elif_algo = PrimesToNth(int(sum_of_float_list))
        arda_algo = PrimesToNth(int(sum_of_float_list))
        vict_algo = PrimesToNth(int(sum_of_float_list))

        # O(n)
        print("\nAlix's Eratosthenes Prime Sieve: ")
        print(f"All Prime Numbers to {sum_of_float_list}:\n {alix_algo.eratosthenes_sieve()}")

        alix_time_taken = timeit.timeit("alix_algo.eratosthenes_sieve()", globals=globals(), number=no_of_times)
        print("Timeit:\t", alix_time_taken / no_of_times)

        # 0(n**2)
        print("\nElifsu's Iterative Prime Checker: ")
        print(f"All Prime Numbers to {sum_of_float_list}:\n {elif_algo.all_primes_to_nth()}")

        elif_time_taken = timeit.timeit("elif_algo.all_primes_to_nth()", globals=globals(), number=no_of_times)
        print("Timeit:\t", elif_time_taken / no_of_times)

        # 0(n**2)
        print("\nArda's Iterative Prime Checker: ")
        print(f"All Prime Numbers to {sum_of_float_list}:\n {list(arda_algo.prime_generator())}")

        arda_time_taken = timeit.timeit("list(arda_algo.prime_generator())", globals=globals(), number=no_of_times)
        print("Timeit:\t", arda_time_taken / no_of_times)

        # 0(n**2)
        print("\nVictoria's Iterative Prime Checker: ")
        print(f"All Prime Numbers to {sum_of_float_list}:\n {vict_algo.create_primes()}")

        vict_time_taken = timeit.timeit("vict_algo.create_primes()", globals=globals(), number=no_of_times)
        print("Timeit:\t", vict_time_taken / no_of_times)

        # add times to list for y axis plot
        alix_list_of_times.append(alix_time_taken / no_of_times)
        arda_list_of_times.append(elif_time_taken / no_of_times)
        elifsu_list_of_times.append(arda_time_taken / no_of_times)
        victoria_list_of_times.append(vict_time_taken / no_of_times)

        # add current input total to list for x axis
        sum_of_floats_x_axis.append(sum_of_float_list)

        # increase input
        sum_of_float_list *= 2

    # plt.style.use("ggplot")
    with plt.xkcd():
        plt.xlabel('Input')
        plt.ylabel('Time')
        plt.plot(sum_of_floats_x_axis, alix_list_of_times, label="Alix - E.Sieve 0(n)")
        plt.plot(sum_of_floats_x_axis, arda_list_of_times, label="Arda - Iteration 0(**2)")
        plt.plot(sum_of_floats_x_axis, elifsu_list_of_times, label="Elifsu - Iteration 0(n**2)")
        plt.plot(sum_of_floats_x_axis, victoria_list_of_times, label="Victoria - Iteration 0(n**2)")
        plt.legend()
        plt.show()

    # End
