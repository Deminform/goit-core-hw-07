from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e.args[0] if not e.args[0].startswith('not') else "Enter the argument for the command."
        except KeyError:
            return "KeyError."
        except IndexError as e:
            return e.args[0] if not e.args[0].startswith('list') else "Enter the argument for the command"

    return inner
