def calculate_total_time_to_run(func):
    """
    This decorator calculates the time your functions takes to execute.
    """
    def inner(*args, **kwargs):
        import time
        start = time.perf_counter()
        func(*args, **kwargs)
        print(f'\033[96mEXECUTED IN {time.perf_counter() - start:.2f}s\033[0m')
    return inner


def show_time_breakdown(func):
    """
    Breaks down your function in terms of maximum time-taking areas of code
    """
    def inner(*args, **kwargs):
        import cProfile
        import pstats
        with cProfile.Profile() as pr:
            func(*args, **kwargs)
        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
    return inner


if __name__ == '__main__':
    # If the file is run as a script, do nothing
    pass
