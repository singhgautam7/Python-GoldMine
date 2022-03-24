# Installation
```
pip install c_out
```


# Introduction  

**Colored Output - c_out**  

You don't have to tell me how monotonous it is to use the same old print statement in python, as there is no option to format it. Moreover, we all have faced problems while debugging our code with countless print statements but no way to highlight any of it.

Well we can definitely install/import third-party packages, but some of us just prefer the old school solutions.

I have a simple, yet effective solution for you.
What if I tell you, it is possible to create a custom class yourself which can format the output in the terminal?

Using this module you can directly format the output you see in your command line interface **without using any external packages**.  
It uses **ANSI Escape Codes** to format the standard output.
  
## Example Usage  
  

    c_out("Hello World")  
    c_out("Hello World", Color.Text.BLUE)  
    c_out("Hello World", Color.Text.RED, Color.BG.BLACK, Style.BOLD)  
    c_out("Hello World", Color.Text.RED, Color.BG.BLACK, Style.BOLD, Style.STRIKETHROUGH)  
    c_out("Hello World", Color.Text.RED, Color.BG.BLACK, Style.BOLD, Style.STRIKETHROUGH, Style.ITALIC) 

 

