import functools
import time


def cache(times):

    def decorator(f):
        cache_obj = {}

        @functools.wraps(f)
        def wrapper(*args):
            if f not in cache_obj:
                cache_obj[f] = time.time()
                print(f"Data {f}, add in cache")
            else:
                if time.time() - cache_obj[f] > times:
                    del cache_obj[f]
                    print(f"Data {f}, left time range")
            return f(*args)

        return wrapper
    return decorator
