'''Instead of writing a function like this,
You can also write it in a different way, to make it clear'''
def greet() -> None:
    print('Hello, world!')

def bye() -> None:
    print('Bye, world!')


def main() -> None:
    greet('Hello, world')
    bye('Bye, world')

if __name__ == '__main__':
    
    main()

