# Introduction  

**Colored Output = c_out**  

You don't have to tell me how monotonous it is to use the same old print statement in python, as there is no option to format it. Moreover, we all have faced problems while debugging our code with countless print statements but no way to highlight any of it.

Well we can definitely install/import third-party packages, but some of us just prefer the old school solutions.

I have a simple, yet effective solution for you.
What if I tell you, it is possible to create a custom class yourself which can format the output in the terminal?

Using this module you can directly format the output you see in your command line interface **without using any external packages**.  
It uses **ANSI Escape Codes** to format the standard output.
  
# Installation
```
pip install c_out
```

# Usage

## Import
```python
from c_out.beauty_print import c_out, TextColor, BackgroundColor, Style
```

## Different Ways to use

#### Normal print
```python
c_out("Hello World")  
```

#### Print with just text color
```python
c_out("Hello World", text_color=TextColor.BLUE)  
```

#### Print with just background color
```python
c_out("Hello World", bg_color=BackgroundColor.BLACK)  
```

#### Print with text color and background color
```python
c_out("Hello World", text_color=TextColor.RED, bg_color=BackgroundColor.BLACK, styles=[Style.BOLD])  
```

#### Print with text color, background color and font styles
```python
c_out("Hello World", text_color=TextColor.RED, bg_color=BackgroundColor.BLACK, styles=[Style.BOLD])  
c_out("Hello World", text_color=TextColor.RED, bg_color=BackgroundColor.BLACK, styles=[Style.BOLD, Style.STRIKETHROUGH, Style.ITALIC])
```

#### Print with separator and text color
```python
c_out("Hello", "World", text_color=TextColor.RED, sep='\n')  
```

#### Print with end of line and text color
```python
c_out("Hello", "World", text_color=TextColor.RED, end='\t')  
```


And there are many more combinations that you can try yourself.


# Choices

### Current Choices for TextColor
- BLACK
- RED
- GREEN
- ORANGE
- BLUE
- PURPLE
- CYAN
- LIGHTGREY
- DARKGREY
- LIGHTRED
- LIGHTGREEN
- YELLOW
- LIGHTBLUE
- PINK
- LIGHTCYAN

### Current Choices for BackgroundColor
- BLACK
- RED
- GREEN
- ORANGE
- BLUE
- PURPLE
- CYAN
- LIGHTGREY

### Current choices for Styles
- BOLD
- UNDERLINE
- ITALIC
- STRIKETHROUGH
- SELECTED
