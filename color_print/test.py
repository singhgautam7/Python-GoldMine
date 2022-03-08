def print_format_table():
    """
    This method prints all the combinations of background and text colors.
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 48):
                fmt = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (fmt, fmt)
            print(s1)
        print('\n')


if __name__ == '__main__':
    print_format_table()
