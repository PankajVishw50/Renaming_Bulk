import constant as c
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, commondialog, simpledialog


class Window:
    def __init__(self, app):
        self.app = app
        app.geometry(f"{c.DIS_WIDTH}x{c.DIS_HEIGHT}")
        app.resizable(False, False)

        self.setup()

    def setup(self):
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


        self.main_frame = LabelFrame(self.app, relief="ridge", border=1)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=True, padx=25, pady=25)

        loc_placeholder = ttk.Entry(self.main_frame, width=100, textvariable=self.loc_value,
                                    )
        loc_placeholder.grid(row=0, column=0, columnspan=2, padx=(175, 10), pady=25)

        open_button = ttk.Button(self.main_frame, text="Open",
                                 command=lambda: [self.openDialog()])

        open_button.grid(row=0, column=2, ipady=10, ipadx=20)

        atStart_option = ttk.Checkbutton(self.main_frame, text="Add Text at Start", variable=self.atStart_value)
        atEnd_option = ttk.Checkbutton(self.main_frame, text="Add Text at End", variable=self.atEnd_value)
        custom_option = ttk.Checkbutton(self.main_frame, text="Add Text after n Character",
                                        variable=self.custom_value)

        atStart_option.grid(row=1, column=0, pady=(25, 10))
        atEnd_option.grid(row=1, column=1, pady=(25, 10))
        custom_option.grid(row=1, column=2, pady=(25, 10))

        atStart_text = ttk.Entry(self.main_frame, textvariable=self.atStart_text_var)
        atEnd_text = ttk.Entry(self.main_frame, textvariable=self.atEnd_text_var)
        custom_text = ttk.Entry(self.main_frame, textvariable=self.custom_text_var)
        number_text = ttk.Entry(self.main_frame, width=5, textvariable=self.number_text_var)

        atStart_text.grid(row=2, column=0, pady=(0, 25))
        atEnd_text.grid(row=2, column=1, pady=(0, 25))
        custom_text.grid(row=2, column=2, pady=(0, 25))
        number_text.grid(row=2, column=3, pady=(0, 25))

        choices_label = ttk.Label(self.main_frame, text="Target File Type ")
        self.drop_box = ttk.Combobox(self.main_frame, values=self.drop_box_values, justify=CENTER)
        self.drop_box.current(0)

        choices_label.grid(row=3, column=0)
        self.drop_box.grid(row=3, column=1)

        totalFile_placeholder = ttk.Label(self.main_frame, text="Total File:", font=("@Adobe Heiti Std R", 13))
        totalFiles_label = ttk.Label(self.main_frame, textvariable=self.totalFiles)

        totalFile_placeholder.grid(row=4, column=0, pady=100)
        totalFiles_label.grid(row=4, column=1)

        self.rename_button = ttk.Button(self.main_frame, text="Rename")
        self.rename_button.grid(row=5, column=1, ipadx=10, ipady=10)

    def openDialog(self):
        filebox = filedialog.askdirectory(initialdir=c.INIT_DIR)
        self.loc_value.set(filebox)

        print(filebox)
