import shutil
import argparse

from os import getcwd
from os.path import expanduser
from pathlib import Path

HOME=expanduser("~")
PWD=getcwd()

files = {
            (".config/kitty", "config/kitty/")
        }

def print_dir():
    print("home: " + HOME)
    print("PWD: " + PWD)
    [print("from \"" + file[0] + "\" to \"" + file[1] + "\"") for file in files]

def collect_file():
    for file in files:
        print("collect: " + PWD + "/" + file[1])
        Path(PWD + "/" + file[1]).mkdir(parents=True, exist_ok=True)
        shutil.copy();
    return

def install_file():
    print("install")
    return

def main():
    parser = argparse.ArgumentParser(
                    prog = 'python setup.py',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')

    parser.add_argument('-c', '--collect', type=str, nargs='?', const='all', help='collect config file')
    parser.add_argument('-i', '--install', type=str, nargs='?', const='all', help='install config file')

    args = parser.parse_args()

    if (args.collect):
        collect_file()
    elif (args.install):
        install_file()

if __name__ == '__main__':
    main()
