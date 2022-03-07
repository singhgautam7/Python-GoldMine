def print_total_time_to_run(target_function, *args, **kwargs):
    """
    Calculate the time your functions takes to execute.
    This will just give you the total time it takes but not 
    the breakdown of slow pieces of code inside your funtion
    
    You can just import this function and pass your function as an
    argument. 

    Args:
        target_function: your function you want to calculate the elapsed 
            time for.
        *args: arguments passed in your function (if any)
        **kwargs: keyword arguments passed in your function (if any)
    """
    import time
    start = time.perf_counter()

    # Disabling target_function to print anything
    target_function(*args, **kwargs)

    print(f'executed in {time.perf_counter() - start:.2f}s')


def print_time_breakdown(target_function, *args, **kwargs):
    """
    This will break down your function in terms of maximum time-
    taking areas of code
    
    You can just import this function and pass your function as an
    argument. 

    Args:
        target_function: your function you want to calculate the elapsed 
            time for.
        *args: arguments passed in your function (if any)
        **kwargs: keyword arguments passed in your function (if any)
    """
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        target_function(*args, **kwargs)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


if __name__ == '__main__':
    # If the file is run as a script, do nothing
    pass
