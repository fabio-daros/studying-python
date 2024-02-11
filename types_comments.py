"""
Types in comments.

"""
import math


# Example_1 Unique arg ----------------------------------------------------------------
def circumference(radius):
    # type: (float) -> float
    return 2 * math.pi * radius


print(circumference(8))


# Example_2 multiples args ----------------------------------------------------------------

def header_1(text, alignment=True):
    # type: (str, bool) -> str
    if alignment:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, '#')


# Example_3 multiples args in the same line ----------------------------------------------------------------
def header_2(
        text,  # type: str,
        alignment=True,  # type: bool
):  # type: (...) -> str
    if alignment:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, '#')
