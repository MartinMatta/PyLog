from colors import *
import datetime


class Log(object):

    def __init__(self):
        self.log = list()

    def e(self, text, tag="ERROR", color=RED):  # error
        self.format_text(tag, color, text)

    def d(self, text, tag="DEBUG", color=CYAN):  # debug
        self.format_text(tag, color, text)

    def i(self, text, tag="INFO", color=BLUE):  # info
       self.format_text(tag, color, text)

    def v(self, text, tag="VERBOSE", color=YELLOW):  # verbose
        self.format_text(tag, color, text)

    def w(self, text, tag="WARN", color=MAGENTA):  # warn
        self.format_text(tag, color, text)

    def format_text(self, tag, color, text):
        time = datetime.datetime.now()
        _text = str(time) + " [" + tag + "] " + text

        print(color + _text + ENDC)
        self.log.append(_text + "\n")

    def close(self, save=True, filename="./out_log.txt"):

        if save:
            with open(filename, "a") as file:
                for i in self.log:
                    file.write(i)

                file.close()

        else:
            pass
