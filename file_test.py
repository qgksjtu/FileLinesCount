"""
================================================================

   Editor      : Jupyter Notebook
   File name   : file_test.py
   Author      : Guangkai Qiao
   Created date: 2022-09-27
   Description : The unit test of the task.

================================================================
"""
import unittest
import os
import random
import shutil
from file_count import FileCollection


def create_file(target, lines):
    """
    Tools that to create a files with given lines.
    Input:
        target: the directory of the file;
        lines: the number of lines to create.
    """
    file_d = open(target, "w")
    for _ in range(lines):
        file_d.write('\n')
    file_d.close()


class TestCountFiles(unittest.TestCase):
    """
    The Unit Test Class.
    """
    def test_count_files_success(self):
        """
        Test whether the program can successfully calculate the lines.
        """
        for _ in range(1, 10):
            if os.path.exists("./test/"):
                shutil.rmtree("./test/")
            os.mkdir("./test/")
            file_lengths = [random.randint(1, 100) for j in range(5)]
            create_file("./test/0.txt", file_lengths[0])
            create_file("./test/1.txt", file_lengths[1])
            os.mkdir("./test/test_sub1/")
            create_file("./test/test_sub1/2.txt", file_lengths[2])
            os.mkdir("./test/test_sub2/")
            create_file("./test/test_sub1/3.txt", file_lengths[3])
            os.mkdir("./test/test_sub1/test_sub1_sub1/")
            os.mkdir("./test/test_sub1/test_sub1_sub2/")
            create_file("./test/test_sub1/test_sub1_sub2/4.txt", file_lengths[4])

            file_collection = FileCollection()
            file_collection.count("./test")

            for i in range(5):
                self.assertEqual(file_collection.file_list[i].lines, file_lengths[i])

            self.assertEqual(file_collection.total_lines, sum(file_lengths))

    def test_count_empty_files_success(self):
        """
        Test whether the program can successfully calculate with empty contents.
        """
        if os.path.exists("./test/"):
            shutil.rmtree("./test/")
        os.mkdir("./test/")
        file_lengths = [0 for j in range(5)]
        create_file("./test/0.txt", file_lengths[0])
        create_file("./test/1.txt", file_lengths[1])
        os.mkdir("./test/test_sub1/")
        create_file("./test/test_sub1/2.txt", file_lengths[2])
        os.mkdir("./test/test_sub2/")
        create_file("./test/test_sub1/3.txt", file_lengths[3])
        os.mkdir("./test/test_sub1/test_sub1_sub1/")
        os.mkdir("./test/test_sub1/test_sub1_sub2/")
        create_file("./test/test_sub1/test_sub1_sub2/4.txt", file_lengths[4])

        file_collection = FileCollection()
        file_collection.count("./test")

        for i in range(5):
            self.assertEqual(file_collection.file_list[i].lines, 0)

        self.assertEqual(file_collection.total_lines, 0)

    def test_count_empty_folders_success(self):
        """
        Test whether the program can successfully calculate with empty subfolders.
        """
        if os.path.exists("./test/"):
            shutil.rmtree("./test/")
        os.mkdir("./test/")
        os.mkdir("./test/test_sub1/")
        os.mkdir("./test/test_sub2/")
        os.mkdir("./test/test_sub1/test_sub1_sub1/")
        os.mkdir("./test/test_sub1/test_sub1_sub2/")

        file_collection = FileCollection()
        file_collection.count("./test")

        self.assertEqual(file_collection.file_list, [])
        self.assertEqual(file_collection.total_lines, 0)

    def test_count_large_files_success(self):
        """
        Test whether the program can successfully calculate with large files.
        """
        for _ in range(1, 10):
            if os.path.exists("./test/"):
                shutil.rmtree("./test/")
            os.mkdir("./test/")
            file_lengths = [random.randint(500000, 1000000) for j in range(5)]
            create_file("./test/0.txt", file_lengths[0])
            create_file("./test/1.txt", file_lengths[1])
            os.mkdir("./test/test_sub1/")
            create_file("./test/test_sub1/2.txt", file_lengths[2])
            os.mkdir("./test/test_sub2/")
            create_file("./test/test_sub1/3.txt", file_lengths[3])
            os.mkdir("./test/test_sub1/test_sub1_sub1/")
            os.mkdir("./test/test_sub1/test_sub1_sub2/")
            create_file("./test/test_sub1/test_sub1_sub2/4.txt", file_lengths[4])

            file_collection = FileCollection()
            file_collection.count("./test")

            for i in range(5):
                self.assertEqual(file_collection.file_list[i].lines, file_lengths[i])

            self.assertEqual(file_collection.total_lines, sum(file_lengths))
