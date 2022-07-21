from tkinter import *
from tkinter import filedialog, simpledialog
from gui import *
from action import *


def run(app):
    display = Window(app)


if __name__ == "__main__":
    root = Tk()

    run(root)

    root.mainloop()
