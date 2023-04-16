class MnemoToNumber:
    def __init__(self, input_mnemo, file_reader):
        split_mnemo = input_mnemo.strip().lower().split(" ")

        key = list()
        for i in split_mnemo:
            for k, v in file_reader.items():
                if i == v:
                    key.append(k)

        self.number = "".join(key)

    def get_number(self):
        return self.number
