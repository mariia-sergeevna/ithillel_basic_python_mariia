from homework_17.script_phone_book import verbose


def display_status(func):
    def wrapper(*args, **kwargs):
        if verbose:
            print("Starting handle your request...")
        result = func(*args, **kwargs)
        if verbose:
            print("Request handled is finished.")
        return result

    return wrapper
