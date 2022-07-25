import os
from tkinter import messagebox


class Rename:

    def rename_files(self, dir_location, text, file_type="All files"):

        self.successful = 0

        try:
            if self.check_isDir(dir_location):    # Verifying if location is Dir
                files_collections = os.listdir(dir_location)
                print(files_collections)

                for index, file in enumerate(files_collections):
                    file_loc = os.path.join(dir_location, file)

                    if self.check_isFile(file_loc):     # Verifying if file_loc is file
                        oFile_in_part = file.split(".")

                        # Verifying if file is eligible for rename process
                        if file_type == "All files" or oFile_in_part[-1].lower() == file_type.lower():
                            new_name = file
                            if text["Start"]:
                                new_name = text["Start"] + file

                            if text["End"]:
                                file_in_part = new_name.split(".")
                                file_in_part[0] += text["End"]
                                new_name = file_in_part[0]

                                for part in file_in_part[1:]:
                                    new_name += "." + part

                            new_file_location = os.path.join(dir_location, new_name)
                            os.rename(file_loc, new_file_location)
                            self.successful += 1

                # This condition checks if user really provides input text to rename files
                # hence not showing message when user haven't provided any input
                if text["Start"] != "" or text["End"] != "":
                    messagebox.showinfo("Successful", "Process Completed successfully ")

            else:
                return False

        except Exception as e:
            return False

        return True

    @staticmethod
    def check_isDir(location):
        return os.path.isdir(location)

    @staticmethod
    def check_isFile(location):
        return os.path.isfile(location)

    @staticmethod
    def count_files(location):
        try:
            items = os.listdir(location)
            total_files = 0

            if not os.path.isdir(location):
                return 0     # 0 means some Error occured

            for x in items:
                path = os.path.join(location, x)
                if os.path.isfile(path):
                    total_files += 1

            return total_files

        except Exception as e:
            messagebox.showinfo("Error", f"*{e}\nPlease fix this problem or choose other DIR")
            return "Error"

    def find_extensions(self, location):
        try:
            all_files = os.listdir(location)
            extensions = {"All files"}

            for item in all_files:
                path = os.path.join(location, item)
                if self.check_isFile(path):
                    inParts = item.split(".")
                    value = inParts[-1]

                    if len(inParts) >= 2:
                        extensions.add(value)

            extensions = list(extensions)
            return extensions

        except Exception as e:
            messagebox.showinfo("Error", f"{e}")
