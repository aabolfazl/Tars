#!/usr/bin/env python3


import argparse
import sys

from LogReader import LogReader


def main():
    if len(sys.argv) < 2:
        print("Usage: python logreader.py <file_path> <param2> ...")
        sys.exit(1)

    parser = argparse.ArgumentParser(description='Process some files and parameters.')

    parser.add_argument('-i', '--input', type=str, help='The input file or directory path', required=True)
    parser.add_argument('-t', '--tags', nargs='+', help='List of tags', required=False)
    parser.add_argument('-m', '--messages', nargs='+', help='List of messages', required=False)
    parser.add_argument('-o', '--output', type=str, help='The output file path', required=False)
    parser.add_argument('-e', '--exception', type=str, help='Show exception', required=False, default=False)

    args = parser.parse_args()
    reader = LogReader(args)
    reader.start()


if __name__ == '__main__':
    main()
