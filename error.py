"""
Errors most commons

"""
"""
printf('Hello World')

Traceback (most recent call last):
  File "/Users/darosfabio/PycharmProjects/guppe/error.py", line 6, in <module>
    printf('Hello World')
    ^^^^^^
NameError: name 'printf' is not defined. Did you mean: 'print'?
"""

# Examples 1 -> SyntaxError

"""
1. def function
    print('Hello World')
    
2. def = 1

3. Only: return

"""

# Examples 2 -> NameError -> When a variable or function not be defined.

"""
1. print(geek)

Traceback (most recent call last):
  File "/Users/darosfabio/PycharmProjects/guppe/error.py", line 29, in <module>
    print(geek)
          ^^^^
NameError: name 'geek' is not defined

2. geek()

3. a = 8
    if a < 10:
        msg = 'Greater than 10'
 File "/Users/darosfabio/PycharmProjects/guppe/error.py", line 46
    if a < 10:
IndentationError: unexpected indent

"""
