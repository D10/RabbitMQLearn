

class NumCounter:

    def __init__(self):
        self.number_1 = None
        self.number_2 = None

    def __call__(self, *args, **kwargs):
        if all([self.number_1, self.number_2]):
            result = self.count()
            self.number_1, self.number_2 = None, None
            print(f'----COUNT RESULT {result}')
            return result

    def count(self):
        return self.number_1 + self.number_2


num_counter = NumCounter()
