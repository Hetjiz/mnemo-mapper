from FileReader import FileReader

if __name__ == '__main__':
    file_reader = FileReader()
    if file_reader is None:
        exit()

while True:

    t = input('\n Do you want to insert a number(n) or words(w)?')

    if t == 'n':
        input_number = input('\n Enter number: ')

        if not input_number.isdigit():
            print('You fucked up! NUMBERS idiot!')
            continue

        split_number = [input_number[i:i + 2] for i in range(0, len(input_number), 2)]

        print(" ".join([file_reader[i] for i in split_number]).strip())
        # TODO
        #   String pattern for ChatGPT API:
        #   Erstelle einen Satz mit den folgenden Wörtern in der Reihenfolge: Bier, Keule, Lee

    elif t == 'w':
        # TODO
        print("bla")
    else:
        print("WTF are you dumb?! It's n or w!!!!")



