import os, shutil, argparse
from os.path import join, getsize

parser = argparse.ArgumentParser(description='Remove empty directories from a user-defined location')
parser.add_argument("folder", nargs=1, type=str,
        help="folder to be searched for empty subfolders")
parser.add_argument("-s", "--size", nargs="?", const=1, default=1, type=int,
        help="user-specified number of kilobytes, the program will delete anything smaller than this")
args = parser.parse_args()

DIR = args.folder[0]
MAX_DIR_SIZE_IN_KB = args.size

def get_dir_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            filepath = join(dirpath, filename)
            total_size += getsize(filepath)
    return total_size


found_dirs = []
number_of_found_dirs, total_size = 0, 0
for dirpath, dirnames, filenames in os.walk(DIR, topdown=False):
    for dirname in dirnames:
        current_dirpath = join(dirpath, dirname)
        current_dirsize = get_dir_size(current_dirpath)
        if current_dirsize < MAX_DIR_SIZE_IN_KB * 1024:
            print(current_dirpath)
            found_dirs.append(current_dirpath)
            number_of_found_dirs += 1
            total_size += current_dirsize

if found_dirs:
    delete = raw_input("Do you want to delete the above directories [y/n]?")

    if delete != "y":
      exit()
    else:
        for dirpath in found_dirs:
            shutil.rmtree(dirpath, ignore_errors = False)
            print(dirpath, 'removed')

        print(number_of_found_dirs, 'directories removed')
        print(total_size/1024, 'kilobytes removed') 
