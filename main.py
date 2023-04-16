from components.FileReader import FileReader
from components.NumbersToMnemo import NumbersToMnemo


def numbers_to_mnemo_module():
    input_number = input('\n Enter number: ')

    if not input_number.isdigit():
        print('You fucked up! NUMBERS idiot!')
        return

    numbers_to_mnemo = NumbersToMnemo(input_number, file_reader)
    print(numbers_to_mnemo.get_split_number())


# START HERE
if __name__ == '__main__':
    file_reader = FileReader()
    if file_reader is None:
        exit()

while True:
    branch = input('\n Do you want to insert a number(n) or words(w)? ')

    if branch == 'n':
        numbers_to_mnemo_module()

    elif branch == 'w':
        # TODO
        print("bla")
    else:
        print("WTF are you dumb?! It's n or w!!!!")
