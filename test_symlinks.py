#!/bin/python

import os
import sys

def get_dead_symliks(top):
    symlinks = []
    for root, _, files in os.walk(top):
        for file in files:
            abs_path = os.path.join(root, file)
            if os.path.islink(abs_path) and not os.path.exists(abs_path):
                symlinks.append(abs_path)
    return symlinks


def main(argv):
    top = '.'
    if len(argv) > 1:
        if not os.path.exists(argv[1]):
            print("'{}' does not seem to exist!".format(argv[1]))
            sys.exit(2)
        top = argv[1]

    symlinks = get_dead_symliks(top)
    if symlinks:
        for abs_path in symlinks:
            print("Broken symbolic link {}".format(abs_path))
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main(sys.argv)
