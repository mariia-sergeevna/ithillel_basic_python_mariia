from functools import wraps


def verbose_mode(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        is_verbose = getattr(self, "verbose", False)
        if is_verbose:
            print(f"Starting handle your request...")

        result = func(self, *args, **kwargs)

        if is_verbose:
            print(f"Request handled is finished.")

        return result

    return wrapped
