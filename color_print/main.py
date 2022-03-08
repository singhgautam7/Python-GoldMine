class Color:
    """
    Keys for formatting print statements
    """
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\33[3m'
    STRIKETHROUGH = '\033[09m'
    URL = '\33[4m'
    BLINK = '\33[5m'
    SELECTED = '\33[7m'

    class Text:
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

    class BG:
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


class Prettify:

    @staticmethod
    def print(text, text_color='', bg_color='', *style):
        """
        The method to print the desired text.
        Note: None of the value should be None
        Args:
            text: <str> text you want to print
            text_color: <Color.Text> color of text
            bg_color: <Color.BG> background color
            *style: <Color> text style like bold, underline etc.
        Returns: None
        Examples:
            To print a text with red color, bold style and black background -
                Prettify.print("Hello World", Color.Text.RED, Color.BG.BLACK, Color.BOLD)
        """
        format_end = '\033[0m'
        print(f'{text_color.strip()}{bg_color.strip()}{"".join(style)}{text}{format_end}')
