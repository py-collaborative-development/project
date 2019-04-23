import datetime
from threading import Thread, Event


class CanBeConfigured():
    def __init__(self):
        pass
    def configure(self, text, *args, **kwargs):
        return

class MyThread(Thread):
    def __init__(self, event, root):
        Thread.__init__(self)
        self.stopped = event
        self.root = root

    def run(self):
        while not self.stopped.wait(1):
            self.root.update_clock()

class Timer():
    def __init__(self):
        self.label = CanBeConfigured()
        self.begin = datetime.datetime.now()
        self.delta = 0

        self.update_clock()
        self.stopped = Event()
        self.thread = MyThread(self.stopped, self)
        self.thread.start()

    def update_clock(self):
        self.delta = datetime.datetime.now() - self.begin
        self.label.configure(text= '{:0>2}:{:0>2}'.format(self.delta.seconds // 60, self.delta.seconds % 60) )

    def stop_clock(self):
        self.stopped.set()


def bomb():
    print("YOU ARE DEAD!!!")


def none():
    print("Nothing")


def number(num):
    def print_number():
        print("Number ", num)
    return print_number
