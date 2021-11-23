# Итератор.

class FibonacciGenerator:
    def __init__(self, limit):
        self.prev = 0  # предыдущее число
        self.cur = 1  # текущее число фибоначчи
        self.limit = limit
        self.i = 0  # итерация

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.limit:
            result = self.prev
            self.prev, self.cur = self.cur, self.prev + self.cur
            self.i += 1
            return result
        else:
            raise StopIteration


for i in FibonacciGenerator(100):
    print(i)

print('\n-----------------\n')

# Генератор.

def fibonacciGenerator(limit):
    prev = 0
    cur = 1
    count = 0

    while count < limit:
        result = prev
        prev, cur = cur, prev + cur
        count += 1
        yield result


for item in fibonacciGenerator(35):
    print(item)
