# Question 1: sort list without creating another list as per give order
# input list=[12345,"Happy","very",1234,"I","am",1,12,123,"excited" ]
# output list=[1,12,123,1234,12345,"I","am","very","Happy","excited"]
import main


def key_function(x):
    if isinstance(x, int):
        return


@main.calculate_total_time_to_run
def custom_sort(ip_list):
    return sorted(
        ip_list,
        key=lambda x:
        (str(x).isalpha(), len(str(x))),
    )


if __name__ == '__main__':

    ip = [12345, "Happy", "very", 1234, "I", "am", 1, 12, 123, "excited"]
    print("input", ip)
    custom_sort(ip)
    # main.print_time_breakdown(custom_sort, ip)
