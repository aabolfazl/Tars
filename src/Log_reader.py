#!/usr/bin/env python3


import argparse
import sys

from LogReader import LogReader


def main():
    if len(sys.argv) < 2:
        print("Usage: python logreader.py <file_path> <param2> ...")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Process some files and parameters.')

    parser.add_argument('input_file', type=str, help='The input file path')
    parser.add_argument('-t', '--tags', nargs='+', help='List of tags')
    parser.add_argument('-o', '--output_file', type=str, help='The output file path')

    args = parser.parse_args()
    reader = LogReader(args)
    reader.start()


if __name__ == '__main__':
    main()
