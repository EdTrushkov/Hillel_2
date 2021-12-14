import functools
import time


def cache(N):
    memory = {}

    @functools.wraps(N)
    def check_time(*args):
        for i in args:
            if i not in memory:
                memory[i] = time.time()
            elif i in memory:
                if time.time() - memory[i] < i:
                    print(i, memory[i])
                else:
                    del memory[i]
    return check_time


@cache
def N(times):
    return times
