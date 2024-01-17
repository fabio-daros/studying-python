def function_1():
    print('Hello World . first.py')


if __name__ == '__main__':
    function_1()
    print('first.py has been executed')
else:
    print(f'first.py has been imported. {__name__}')
