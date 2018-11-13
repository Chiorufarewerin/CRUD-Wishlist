'''Main file of program.'''

import sys
from app import MainWindow
import db


def main():
    '''Start application function'''
    MainWindow.start(sys.argv)


if __name__ == '__main__':
    main()
