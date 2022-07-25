import os
import constant as c
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, commondialog, simpledialog, messagebox
from action import Rename


class Window:
    def __init__(self, app):

        # <------------ Tkinter App configuration and settings -------------------->
        self.app = app
        app.title("Renaming Bulk")
        app.geometry(f"{c.DIS_WIDTH}x{c.DIS_HEIGHT}")
        app.resizable(False, False)

        # <------------------- Setting up necessary variables --------------------->
        self.rename_obj = Rename()
        self.dict_values = {"Start": "", "End": "", "Custom": ""}
        self.loc_value = StringVar()
        self.totalFiles = IntVar()

        self.atStart_value = IntVar()
        self.atEnd_value = IntVar()
        self.custom_value = IntVar()

        self.atStart_text_var = StringVar()
        self.atEnd_text_var = StringVar()
        self.custom_text_var = StringVar()
        self.number_text_var = StringVar()

        self.drop_box_values = ["All files"]

        self.setup()

    def setup(self):

        # <----------- GUI Widgets ------------->
        main_frame = LabelFrame(self.app, relief="ridge", border=1)
        main_frame.pack(side=TOP, fill=BOTH, expand=True, padx=25, pady=25)

        loc_placeholder = ttk.Entry(main_frame, width=100, textvariable=self.loc_value,
                                    )
        loc_placeholder.grid(row=0, column=0, columnspan=2, padx=(175, 10), pady=25)

        open_button = ttk.Button(main_frame, text="Open",
                                 command=lambda: [self.openDialog()])

        open_button.grid(row=0, column=2, ipady=10, ipadx=20)

        atStart_option = ttk.Checkbutton(main_frame, text="Add Text at Start", variable=self.atStart_value)
        atEnd_option = ttk.Checkbutton(main_frame, text="Add Text at End", variable=self.atEnd_value)
        custom_option = ttk.Checkbutton(main_frame, text="Add Text after n Character",
                                        variable=self.custom_value,
                                        state=DISABLED)

        atStart_option.grid(row=1, column=0, pady=(25, 10))
        atEnd_option.grid(row=1, column=1, pady=(25, 10))
        custom_option.grid(row=1, column=2, pady=(25, 10))

        atStart_text = ttk.Entry(main_frame, textvariable=self.atStart_text_var)
        atEnd_text = ttk.Entry(main_frame, textvariable=self.atEnd_text_var)
        custom_text = ttk.Entry(main_frame, textvariable=self.custom_text_var, state=DISABLED)
        number_text = ttk.Entry(main_frame, width=5, textvariable=self.number_text_var, state=DISABLED)

        atStart_text.grid(row=2, column=0, pady=(0, 25))
        atEnd_text.grid(row=2, column=1, pady=(0, 25))
        custom_text.grid(row=2, column=2, pady=(0, 25))
        number_text.grid(row=2, column=3, pady=(0, 25))

        choices_label = ttk.Label(main_frame, text="Target File Type ")
        self.drop_box = ttk.Combobox(main_frame, values=self.drop_box_values, justify=CENTER)
        self.drop_box.current(0)

        choices_label.grid(row=3, column=0)
        self.drop_box.grid(row=3, column=1)

        totalFile_placeholder = ttk.Label(main_frame, text="Total File:", font=("@Adobe Heiti Std R", 13))
        totalFiles_label = ttk.Label(main_frame, textvariable=self.totalFiles)

        totalFile_placeholder.grid(row=4, column=0, pady=100)
        totalFiles_label.grid(row=4, column=1)

        self.rename_button = ttk.Button(main_frame, text="Rename")
        self.rename_button.grid(row=5, column=1, ipadx=10, ipady=10)

    def openDialog(self):
        """ Opens dialog box for user to select
            Directory location """
        filebox = filedialog.askdirectory(initialdir=c.INIT_DIR)
        self.loc_value.set(filebox)

        if os.path.isdir(self.loc_value.get()):
            extensions = self.rename_obj.find_extensions(self.loc_value.get())

            self.drop_box_values = extensions
            self.drop_box.config(values=self.drop_box_values)

    def forward(self):
        """ It confirms if user really want to continue
        and provide necessary data files like: self.dict_values"""

        # Counting total files to display on messagebox
        total_files = self.rename_obj.count_files(self.loc_value.get())

        # if there will be any problem in counting files or location value it will stop function
        if total_files == "Error":
            return False

        message = f"Total files: {total_files}\nDo you really want to continue\n(it is not reversible)"

        # Asking user if they want to continue
        if WarningBox.confirm("Rename Files", message):
            # If they agree
            # Preparing Files to send
            self.dict_values = dict()
            if self.atStart_value.get() == 1:
                self.dict_values["Start"] = self.atStart_text_var.get()
            else:
                self.dict_values["Start"] = ""
            if self.atEnd_value.get() == 1:
                self.dict_values["End"] = self.atEnd_text_var.get()
            else:
                self.dict_values["End"] = ""

            self.dict_values["Custom"] = False

        else:
            self.dict_values = {"Start": "", "End": "", "Custom": False}


class WarningBox:
    """
    PopUp window to display important messages
    to user
    """
    active_widget = None

    @staticmethod
    def confirm(title, text):
        see = messagebox.askokcancel(title, text)
        return see

    @staticmethod
    def show_info(title, text):
        messagebox.showinfo(title, text)
