def exc_finder(func):
    """
    This decorator will tell you which kind of exception occurs in your function.
    """
    def inner(*args, **kwargs):
        # Not handling BaseExceptions to avoid catching RunTime errors
        try:
            func(*args, **kwargs)
        except Exception as e:
            import os
            line_num = f'\x1b[6;30;42m line number {e.__traceback__.tb_lineno} \x1b[0m'
            func_name = f'\x1b[6;30;42m {func.__name__} \x1b[0m'
            exc_name = f'\x1b[6;30;42m {e.__class__.__name__} \x1b[0m'
            exc_module_name = f'\x1b[6;30;42m {e.__class__.__module__} \x1b[0m'
            file_name = f'\x1b[6;30;42m {os.path.basename(__file__)} \x1b[0m'
            
            # If module is name is builtins, do not import anything
            if e.__class__.__module__ == 'builtins':
                suggestion_str = f'Just handle the {e.__class__.__name__} in line {e.__traceback__.tb_lineno} using try-except block.'
            
            # Else first import the module and then handle the exception
            else:
                clr_print_purple = '\033[35m{}\033[0m'
                clr_print_red = '\033[31m{}\033[0m'
                from_str = clr_print_purple.format('from')
                import_str = clr_print_purple.format('import')
                module_name_str = clr_print_red.format(e.__class__.__module__)
                exc_name_str = clr_print_red.format(e.__class__.__name__)
                final_str = f'{from_str} {module_name_str} {import_str} {exc_name_str}'
                suggestion_str = f'You need to import the following statment to handle this exception.\n'\
                                 f'(Note: if the suggestion is wrong, please report this to developer)\n\n'\
                                 f'{final_str} \n\nAfter this import you can handle the error in line {e.__traceback__.tb_lineno} '\
                                 f'using try-except block.'
            
            print(
                    f'\nAn exception named {exc_name} from module {exc_module_name} has occurred ' \
                    f'{line_num} of your function {func_name} in your {file_name} file.\n\n'\
                    f'SUGGESTION(s):\n{suggestion_str}\n'
                )
    return inner
