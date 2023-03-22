def verbose_mode(verbose):
    """Add detailed processing info to function depending on verbose"""

    def display_status(func):
        def wrapper(*args, **kwargs):
            if verbose:
                print("Starting handle your request...")
            result = func(*args, **kwargs)
            if verbose:
                print("Request handled is finished.")
            return result

        return wrapper

    return display_status
