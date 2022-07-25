# !/usr/bin/env python

from tkinter import *
from tkinter import filedialog, simpledialog
import gui
import action


def run(app):
    display = gui.Window(app)
    work = action.Rename()

    # Configuring rename_button to bind with work object
    display.rename_button.config(command=lambda: [display.forward(),
                                                  work.rename_files(display.loc_value.get(),
                                                                    display.dict_values,
                                                                    display.drop_box.get()),
                                                  display.dict_values.clear()]
                                 )

if __name__ == "__main__":

    root = Tk()
    run(root)

    root.mainloop()
