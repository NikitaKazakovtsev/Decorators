import os
from datetime import datetime
def logger(old_function):

    def new_function(*args, **kwargs):
        my_file = open("main3.log", "a+")
        current_time1 = datetime.now()
        my_file.write(f'{old_function},{args=}, {kwargs=}, {current_time1}')
        value = old_function(*args, **kwargs)
        my_file.write(f', {value}\n')
        return value
    return new_function
@logger
class FlatIterator:

    def __init__(self, list_of_list):
        self.values = list_of_list

    def __iter__(self):
        self.ip1 = 0
        self.ip2 = 0
        return self

    def __next__(self):
        if len(self.values) == self.ip1:
            raise StopIteration
        list_ = self.values[self.ip1]
        item = list_[self.ip2]
        if len(list_) > self.ip2+1:
            self.ip2 += 1
        else:
            self.ip1 += 1
            self.ip2 = 0
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

path = 'main3.log'
if os.path.exists(path):
    os.remove(path)

if __name__ == '__main__':
    test_1()