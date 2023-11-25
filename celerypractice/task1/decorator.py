from celery.exceptions import SoftTimeLimitExceeded, TimeLimitExceeded


def decorator1(func):
    def wrapper(*args, **kwargs):
        try:
            print("ghg")
            return func(*args, **kwargs)
        except SoftTimeLimitExceeded:
            raise TimeLimitExceeded
    return wrapper
