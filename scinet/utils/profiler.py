import cProfile
from functools import partial, wraps


def profile(func=None, number=1, sort="cumtime", verbose=False):

    if not func:
        return partial(profile, number=number, sort=sort, verbose=verbose)

    pr = cProfile.Profile()
    rets = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(number):
            pr.enable()
            ret = func(*args, **kwargs)
            pr.create_stats()
            rets.append(ret)
            if verbose:
                pr.print_stats(sort)
        return rets

    return wrapper
