import sys
import os

PATCHELF = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'patchelf')


def main():
    os.execv(PATCHELF, sys.argv)
