from components.FileReader import FileReader
from components.NumberToMnemo import NumberToMnemo
from components.MnemoToNumber import MnemoToNumber


def number_to_mnemo_module():
    input_number = input("\n Enter number: ")

    if not input_number.isdigit():
        print("You fucked up! NUMBERS idiot!")
        return

    number_to_mnemo = NumberToMnemo(input_number, file_reader)
    print(number_to_mnemo.get_mnemo_words())


def mnemo_to_number_module():
    input_mnemo = input("\n Enter mnemo: ")

    if not input_mnemo.replace(' ', '').isalpha():
        print("No numbers, please!")
        return

    mnemo_to_number = MnemoToNumber(input_mnemo, file_reader)
    print(mnemo_to_number.get_number())


# START HERE
if __name__ == '__main__':
    file_reader = FileReader()
    if file_reader is None:
        exit()

while True:
    branch = input('\n Do you want to insert a number(n) or a mnemonic(m)? ')

    if branch == 'n':
        number_to_mnemo_module()
    elif branch == 'm':
        mnemo_to_number_module()
    else:
        print("WTF are you dumb?! It's n or m!!!!")
