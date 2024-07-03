# Задание №1

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.cursor = 0
        self.subcursor = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.cursor][self.subcursor]
        if self.subcursor == len(self.list_of_list[self.cursor]) - 1:
            self.cursor += 1
            self.subcursor = 0
        else:
            self.subcursor += 1
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()


# Задание №3

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.stack = []

    def __iter__(self):
        self.stack = [(self.list_of_list, 0)]
        return self

    def __next__(self):
        while self.stack:
            current_list, index = self.stack[-1]
            if index == len(current_list):
                self.stack.pop()
                continue
            self.stack[-1] = (current_list, index + 1)
            if isinstance(current_list[index], list):
                self.stack.append((current_list[index], 0))
            else:
                return current_list[index]
        raise StopIteration

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()