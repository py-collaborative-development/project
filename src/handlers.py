import datetime
from threading import Thread, Event


class CanBeConfigured():
    def __init__(self):
        pass
    def configure(self, text, *args, **kwargs):
        return

class MyThread(Thread):
    def __init__(self, event, root, seconds_to_wait):
        Thread.__init__(self)
        self.stopped = event
        self.root = root
        self.seconds_to_wait = seconds_to_wait

    def run(self):
        while not self.stopped.wait(self.seconds_to_wait):
            self.root.update_clock()

class Timer():
    def __init__(self):
        self.label = CanBeConfigured()
        self.begin = datetime.datetime.now()
        self.delta = 0

        self.update_clock()
        self.stopped = Event()
        self.thread = MyThread(self.stopped, self, 1)
        self.thread.start()

    def update_clock(self):
        self.delta = datetime.datetime.now() - self.begin
        self.label.configure(text= '{:0>2}:{:0>2}'.format(self.delta.seconds // 60, self.delta.seconds % 60) )

    def stop_clock(self):
        self.stopped.set()

class Checker():
    def __init__(self, count):
        self.label = CanBeConfigured()
        self.count = count

        self.update_clock()
        self.stopped = Event()
        self.thread = MyThread(self.stopped, self, 0.001)
        self.thread.start()

    def update_clock(self):
        self.label.configure(text= 'Bombs: {}'.format(self.count) )

    def stop_clock(self, win):
        if win == True:
            self.label.configure(text= 'YOU WIN!')
        else:
            self.label.configure(text= 'YOU LOSE!')
        self.stopped.set()


def bomb():
    print("YOU ARE DEAD!!!")


def none():
    print("Nothing")


def number(num):
    def print_number():
        print("Number ", num)
    return print_number
