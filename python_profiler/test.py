# Question 1: sort list without creating another list as per give order
# input list=[12345,"Happy","very",1234,"I","am",1,12,123,"excited" ]
# output list=[1,12,123,1234,12345,"I","am","very","Happy","excited"]

def key_function(x):
    if isinstance(x, int):
        return 
    
def custom_sort(ip_list):
    return sorted(
        ip_list, 
        key=lambda x: 
            (str(x).isalpha(), len(str(x))),
        )


if __name__ == '__main__':
    import profiling
    
    ip = [12345,"Happy","very",1234,"I","am",1,12,123,"excited"]
    print("input", ip)
    profiling.print_total_time_to_run(custom_sort, ip)
    profiling.print_time_breakdown(custom_sort, ip)
