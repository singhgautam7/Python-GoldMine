import json

def _print_all():
    try:
        json.loads('avx')
    except Exception as e:
        print(f'{e.__class__.__name__ = }')
        print(f'{e.__class__.__module__ = }')
        print(f'{__file__ = }')
        print(f'{e.__traceback__.tb_lineno = }')
        print(f'{e.args[0] = }')
        
        import sys
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f'{exc_tb.tb_frame.f_code.co_code = }')
        
        # import traceback
        # print(traceback.format_exc())
    
    
# @exc_finder
# def my_fun():
#     import json
#     json.loads('avx')
    
#     # return 1/0
    
#     # return None.a

        
# if __name__ == '__main__':
#     my_fun()
