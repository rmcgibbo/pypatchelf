import sys
import os.path
import subprocess

PATCHELF = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'patchelf')


def main():
    subprocess.check_output([PATCHELF] + sys.argv[1:])
