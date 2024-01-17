"""
Dunder Name and Dunder Main.

Dunder -> Double under "__x__".

Dunder Name -> __name__
Dunder Main -> __main__

Functions, attributes, property, etc. to not generate conflicts with the names of this element.

In C, we have a program with this form:

int main() {
    return 0;
}

In Java, we have:

public static void main (String[] args) {

}

In Python, if we execute a module in the command line, the Python set to the variable __name__ the value __main__,
and this is the principal module.
"""

# Example_1 ---------------------------

from functions_with_parameter import sum_odd

print(sum_odd([1, 2, 3, 4, 5, 6]))

# Example_2 ---------------------------

