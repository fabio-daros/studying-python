"""
Hint to determine a definitive type to a variable.

"""


# Example_1: ------------------------------------------------------------------------------------------------
def greetings(name: str) -> str:  # here I define the type of data -> String
    return f'Hello, my name is {name}'


print(greetings('[NAME]'))


# Example_2: ------------------------------------------------------------------------------------------------

def header(text: str, alignment: bool = True) -> str:  # Hint Type
    if alignment:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, '#')


print(header('[NAME]'))

print(header('[Alignment False]', alignment=False))
