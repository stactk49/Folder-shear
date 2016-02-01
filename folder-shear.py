import os, shutil, argparse
from os.path import join, getsize

parser = argparse.ArgumentParser(description='Remove empty directories from a user-defined location')
parser.add_argument("folder", nargs=1, type=str,
        help="folder to be searched for empty subfolders")
parser.add_argument("-s", "--size", nargs="?", const=1, default=1, type=int,
        help="user-specified number of kilobytes, the program will delete anything smaller than this")
args = parser.parse_args()

DIR = args.folder[0]
MAX_SIZE = args.size

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            filepath = join(dirpath, filename)
            total_size += getsize(filepath)
    return total_size


found_dirs = []
no_found_dir, total_size = 0, 0
for dirpath, dirnames, filenames in os.walk(DIR, topdown=False):
    for dirname in dirnames:
        current_dirpath = join(dirpath, dirname)
        curr_dir_size = get_size(current_dirpath)
        if curr_dir_size < MAX_SIZE * 1024:
            print(current_dirpath)
            found_dirs.append(current_dirpath)
            no_found_dir += 1
            total_size += curr_dir_size

if found_dirs:
    delete = raw_input("Do you want to delete the above directories [y/n]? ")

    if delete != "y":
      exit()
    else:
        for dirpath in found_dirs:
            shutil.rmtree(dirpath, ignore_errors = False)
            print(dirpath, 'removed')

        print(no_found_dir, 'directories removed')
        print(total_size/1024, 'kilobytes removed') 
