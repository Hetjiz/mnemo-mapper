
class NumbersToMnemo:
    def __init__(self, input_number, file_reader):
        split_number = [input_number[i:i + 2] for i in range(0, len(input_number), 2)]
        self.split_number = " ".join([file_reader[i] for i in split_number]).strip()

    def get_split_number(self):
        return self.split_number

    # TODO
    #   String pattern for ChatGPT API:
    #   Erstelle einen Satz mit den folgenden Wörtern in der Reihenfolge: Bier, Keule, Lee
