"""
Try/except

To treatment of errors in the code. prevent stops in the software.

Example:
    
try:
    // Problematic execution
    
except:
    // In case od problem needs execute...
    
"""

# Example 1 - Generic Errors -------------------------------------------------


try:
    hello()
except:
    print('Any problem occurred')

# Example 2 - Specific treatment -------------------------------------------------

try:
    World()  # If I put "len(5)" in this line for example... the except not be entered because not is a 'NameError'
except NameError:
    print('Nonexistent function utilized')

# Example 3 - With alias -------------------------------------------------

try:
    len(5)
except TypeError as err:
    print(f'The application inform the error: {err}')

# Example 4 - Different types of errors ------------------------------------------

try:
    len(5)
    # hello_3()
except NameError as err_01:
    print(f'Error NameError: {err_01}')
except TypeError as err_02:
    print(f'Error TypeError: {err_02}')


# Example 5 - With dict ------------------------------------------

def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None
    except TypeError:
        return None


dic = {'name': 'Hello'}

print(get_value(dic, 'name'))
