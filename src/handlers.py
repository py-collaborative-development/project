import random
import datetime
from threading import Thread, Event


class MyThread(Thread):
    def __init__(self, root, seconds_to_wait):
        Thread.__init__(self)
        self.daemon = True
        self.root = root
        self.stopped = Event()
        self.seconds_to_wait = seconds_to_wait

    def run(self):
        while not self.stopped.wait(self.seconds_to_wait):
            self.root.update_clock()
        self.join()


class Timer():
    def __init__(self, text_variable):
        self.text_variable = text_variable
        self.reset_clock()
        self.update_clock()
        self.thread = MyThread(self, 1)
        self.thread.start()

    def update_clock(self):
        if self.is_stopped:
            return
        delta = datetime.datetime.now() - self.begin
        text = '{:0>2}:{:0>2}'.format(delta.seconds // 60, delta.seconds % 60)
        self.text_variable.set(text)

    def stop_clock(self):
        self.is_stopped = True

    def reset_clock(self):
        self.begin = datetime.datetime.now()
        self.is_stopped = False
        self.update_clock()


def generate_field(cols, rows, bomb_number):
    '''Generate shema of the field.
    >>> len(generate_field(10, 10, 10))
    100
    >>> len([x for x in generate_field(10, 10, 10) if x < 0])
    10
    >>> max(generate_field(10, 10, 10)) < 9
    True
    '''
    field = [0 for x in range(cols * rows)]
    bomb_indexes = random.sample(range(cols * rows), bomb_number)
    for i in range(bomb_number):
        x = bomb_indexes[i] % rows
        y = bomb_indexes[i] // rows
        for j in range(max(0, x - 1), min(x + 2, rows)):
            for k in range(max(0, y - 1), min(y + 2, cols)):
                index = k * rows + j
                field[index] = field[index] + 1
    for i in range(bomb_number):
        field[bomb_indexes[i]] = -1
    return field
