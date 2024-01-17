import first


def function_2():
    first.function_1()


if __name__ == '__main__':
    function_2()
    print('second.py has been executed')
else:
    print(f'second.py has been imported. {__name__}')
