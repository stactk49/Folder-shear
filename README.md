This program deletes empty folders from a user-specified location. I needed a program like this because when I would recover files from a particularly damaged file system, it would turn up many duplicate files as well as empty folders. When I would run the program "fdupes", it would solve the problem of the duplicate files, but compound the problem of empty folders. In addition, on some Linux systems, even an empty folder reports taking up space when its properties are viewed, usually about 4kb for each. If there are enough empties, it can really add up, leading me to suspect there was a potentially valuable file in there, only to waste time searching for something that wasn't there.

The program was tested on Debian 8 and found to work flawlessly.

syntax: python folder-shear.py -[option] [folder name]

optional arguments: -h, --help show this help message and exit -s [SIZE], --size [SIZE] user-specified number of kilobytes, the program will delete anything smaller than this