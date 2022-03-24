class Style:
    """
    Styling the fonts
    """
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\33[3m'
    STRIKETHROUGH = '\033[09m'
    SELECTED = '\33[7m'


class TextColor:
    """
    Text color/foreground color options
    """
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHTGREY = '\033[37m'
    DARKGREY = '\033[90m'
    LIGHTRED = '\033[91m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHTBLUE = '\033[94m'
    PINK = '\033[95m'
    LIGHTCYAN = '\033[96m'


class BackgroundColor:
    """
    Background color options
    """
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    ORANGE = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    LIGHTGREY = '\033[47m'


def c_out(*args, text_color='', bg_color='', styles=None, sep=' ', end='\n'):
    """
    The method to print the desired text with different colors and styles.
    Args:
        args: all values to be printed
        text_color: <TextColor> color of text
        bg_color: <BackgroundColor> background color
        sep: string inserted between values, default a space.
        end: string appended after the last value, default a newline.
        styles: <list> with values of <Style> class.
    """
    if styles is None:
        styles = []
    format_end = '\033[0m'
    style_str = "".join(styles)
    text = sep.join(str(x) for x in args)
    print(f'{text_color.strip()}{bg_color.strip()}{style_str}{text}{format_end}', end=end)
