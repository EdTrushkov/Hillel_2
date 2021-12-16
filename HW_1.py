import functools
import time


def cache(times):

    def decorator(f):
        cache_obj = {}
        cache_time = {}

        @functools.wraps(f)
        def wrapper(*args):
            if args not in cache_obj:
                cache_obj[args] = f(*args)
                cache_time[args] = time.time()
                print(f"Data {f}, add in cache")
            elif time.time() - cache_time[args] > times:
                cache_obj[args] = f(*args)
                cache_time[args] = time.time()
            return cache_obj[args]

        return wrapper
    return decorator
