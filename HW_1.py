import time
import functools


def cache(N):
    cache_obj = {}

    @functools.wraps(N)
    def cache_func(*args):
        for i in args:
            if i not in cache_obj:
                cache_obj[i] = time.time()
            else:
                if time.time() - cache_obj[i] > N(*args):
                    del cache_obj[i]
                    return f"Data name "{i}", left time range"
        return cache_obj
    return cache_func

@cache
def N(time):
    return time
