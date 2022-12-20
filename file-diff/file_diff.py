import os
import sys


class File:
    def __init__(self, full_path):
        self.full_path = full_path
        self.dir = os.path.dirname(full_path)
        self.file_name = os.path.basename(full_path)
        self.file_size = os.path.getsize(full_path)


class FileDiff:

    def __init__(self, original_dir, compare_dir):
        self.original_dir = original_dir
        self.compare_dir = compare_dir
        self.original_files = {}
        self.compare_files = {}
        self.compare_results = {}

    def main(self):
        self.find_files()
        for k, elem in self.compare_results.items():
            print(f'{k}: name={elem["name"]}, size={elem["size"]} ')

    def find_files(self):
        self.__get_original_files()
        self.__get_compare_files()

        for name, elem in self.original_files.items():
            result = {"name": False, "size": False}
            if name in self.compare_files:
                result["name"] = True
                if elem.file_size == self.compare_files[name].file_size:
                    result["size"] = True

            self.compare_results[name] = result

    def __get_original_files(self):
        for elem in self.__get_files(self.original_dir):
            self.original_files[elem.file_name] = elem

    def __get_compare_files(self):
        for elem in self.__get_files(self.compare_dir):
            self.compare_files[elem.file_name] = elem

    @staticmethod
    def __get_files(top):
        file_list = []
        for root, dirs, files in os.walk(top=top):
            for elem in files:
                file_path = os.path.join(root, elem)
                _file = File(file_path)
                file_list.append(_file)
        return file_list


args = sys.argv
file_diff = FileDiff(args[1], args[2])
file_diff.main()
