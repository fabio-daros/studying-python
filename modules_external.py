"""
External Modules

Utilizing a manager of package call "Pip" or "Python Installer Package"

To know more:

https://pypi.org

Installing the "colorama package" - utilized to print colors text in the terminal.

>>> "pip install NAME_MODULE"

"""
# Example_1 ---------------------------------------------

from colorama import init, Fore, Back

init()

print(Fore.MAGENTA + "Hello World")
print(Fore.BLUE, Back.YELLOW + 'Hello World')

# Example_2 ---------------------------------------------

import pydf

pdf = pydf.generate_pdf('<h1>Hello World</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
