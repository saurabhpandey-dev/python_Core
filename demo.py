def main():
    x = get_input()
    print(f'x is {x}')


def get_input():
    while True:
        try:
            return int(input('enter the value : '))
        except ValueError:
            print('this is not a interger')
        else:
            print('the value')


main()
