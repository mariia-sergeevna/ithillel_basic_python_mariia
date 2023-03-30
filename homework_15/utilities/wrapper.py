from functools import wraps


def verbose_start_and_end(func):
    @wraps(func)
    def wrapped(self, *args, **kwargs):
        is_verbose = getattr(self, 'verbose', False)
        if is_verbose:
            print(f'Starting to process {func.__name__}')

        result = func(self, *args, **kwargs)

        if is_verbose:
            print(f'Finished processing {func.__name__}')

        return result

    return wrapped
