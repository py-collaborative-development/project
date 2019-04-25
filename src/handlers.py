import datetime
from threading import Thread, Event


class CanBeConfigured():
    def __init__(self):
        pass

    def config(self, text, *args, **kwargs):
        return


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
    def __init__(self):
        self.label = CanBeConfigured()
        self.reset_clock()
        self.update_clock()
        self.thread = MyThread(self, 1)
        self.thread.start()

    def update_clock(self):
        if self.is_stopped:
            return
        delta = datetime.datetime.now() - self.begin
        text = '{:0>2}:{:0>2}'.format(delta.seconds // 60, delta.seconds % 60)
        self.label.config(text=text)

    def stop_clock(self):
        self.is_stopped = True

    def reset_clock(self):
        self.begin = datetime.datetime.now()
        self.is_stopped = False
        self.update_clock()


class Checker():
    HAPPY = u"\u263a"
    SAD = u"\u2639"

    def __init__(self, count):
        self.label = CanBeConfigured()
        self.count = count
        self.is_stopped = False

        self.update_clock()
        self.thread = MyThread(self, 0.001)
        self.thread.start()

    def update_clock(self):
        self.label.config(text='Bombs: {}'.format(self.count))

    def stop_clock(self, win):
        if win:
            self.label.config(text=self.HAPPY+'YOU WIN!', fg='green')
        else:
            self.label.config(text=self.SAD+'YOU LOSE!', fg='red')
        self.is_stopped = True
