class NumberToMnemo:
    def __init__(self, input_number, file_reader):
        split_number = [input_number[i:i + 2] for i in range(0, len(input_number), 2)]
        self.mnemo_words = " ".join([file_reader[i].capitalize() for i in split_number]).strip()

    def get_mnemo_words(self):
        return self.mnemo_words

    # TODO
    #   String pattern for ChatGPT API:
    #   Gebrauche die folgenden Wörter in ihrer Reihenfolge, um daraus einen Satz zu bilden: : Bier, Keule, Lee
