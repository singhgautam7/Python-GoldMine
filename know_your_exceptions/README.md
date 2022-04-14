# Introduction

Exception handling is one of the most cruicial part of the coding practices. And it is always a good idea to handle the specific exception using try-except rather than just using the gereral *Exception* class. This package can help you achieve the same. You can find out the exact name of the package and the import statement (if needed) for handling all your exceptions.

# Steps

1. Install the package using `pip install know-your-exceptions`
2. Import the decorator in your file using `from know_your_exceptions.decorators import exc_finder`
3. Add this decorator over your function, and make sure that you function does not have any *try-except* block (so that this package can suggest you accurate exception handling method)

# Example Response

![Example response](https://raw.githubusercontent.com/singhgautam7/Python-GoldMine/master/_assets/know_your_exceptions_example.png)