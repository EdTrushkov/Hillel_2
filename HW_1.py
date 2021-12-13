"""Сделать декоратор cache, который бы кэшировал данные не больше чем на N секунд.
 N должно быть параметром декоратора"""

import time


def cache(N):
    memory = {}

    def check_time(*args):
        if args not in memory:
            memory[args] = time.time()
        elif args in memory:
            if memory[args] - time.time() < N:
                print(memory[args])
    return check_time


