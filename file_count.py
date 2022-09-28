"""
================================================================

   Editor      : Jupyter Notebook
   File name   : file_count.py
   Author      : Guangkai Qiao
   Created date: 2022-09-27
   Description : The core functions of the task.

================================================================
"""
import glob
import queue
import os


def get_file_list(abs_dir, ext=".txt"):
    """
    Get the list of files with required extension like glob.glob() using BFS search.
    Input:
        abs_dir: the directory of the folder;
        ext: required extension.
    Output:
        res: the list of files directories.
    """
    file_queue = queue.Queue()
    file_queue.put(abs_dir)
    res = []
    while not file_queue.empty():
        cur = file_queue.get()

        for i in os.listdir(cur):
            path = os.path.join(cur, i)
            if os.path.isfile(path):
                if path[-len(ext):] == ext:
                    res.append(path)
            else:
                file_queue.put(path)
    return res


class SingleFile():
    """
    The class of a file, which includes the directory of the file and the length of the file.
    """
    def __init__(self, abs_dir, lines):
        """
        Init function of the class.
        Input:
            abs_dir: the directory of the file;
            lines: the number of lines of the file.
        """
        self.abs_dir = abs_dir
        self.lines = lines

    def printer(self):
        """
        Print the directory and the number of lines of the file.
        """
        print(self.abs_dir, '\t', self.lines)

    def get_lines(self):
        """
        Return the number of lines of the file.
        """
        return self.lines


class FileCollection():
    """
    The class of file collection, including the list of SingleFile, total lines of the files,
    the count function, and the printer.
    Usage:
    file_collection = FileCollection()
    file_collection.count(abs_dir, ext, method)
    """
    def __init__(self):
        """
        Init function of the class.
        """
        self.file_list = []
        self.total_lines = 0

    def count(self, abs_dir, ext=".txt", method=""):
        """
        Collect the files in the directory and count the lines of them.
        Input:
            abs_dir: the directory of the folder;
            ext: required extension;
            method: Set method = "glob" to use glob library to collect,
                    otherwise use get_file_list() function.
        """
        if method == "glob":
            find_files = glob.glob(abs_dir + "/**/*" + ext, recursive=True)
        else:
            find_files = get_file_list(abs_dir, ext)

        for i in find_files:
            file_d = open(i, 'r')
            lines = sum(1 for _ in file_d)
            file_d.close()
            singlefile = SingleFile(i, lines)
            singlefile.printer()
            self.file_list.append(singlefile)
            self.total_lines += lines
        self.printer()

    def printer(self):
        """
        Print collected information.
        """
        print("===============")
        print("Number of files found: \t\t", len(self.file_list))
        print("Total number of lines: \t\t", self.total_lines)
        if self.file_list:
            print("Average lines per file: \t",
                  self.total_lines / len(self.file_list))
        else:
            print("Average lines per file: \t", 0.0)
