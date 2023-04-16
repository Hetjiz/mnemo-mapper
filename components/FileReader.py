class FileReader(dict):

    """
    Reading specific mnemonical file and parsing it into a dictionary.
    """
    def __init__(self):
        super().__init__()

        with open("number_word_pairs.txt", 'r') as file:
            for line in file:
                line = line.strip()
                number, word = line.split()
                self[number] = word
