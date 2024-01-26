#!/usr/bin/env python3

import os


class FileHandler:
    def __init__(self, path, mode):
        self._file = None
        self._path = path
        self._mode = mode

    def is_file(self):
        return os.path.isfile(self._path)

    def open_file(self):
        if self._mode not in ['r', 'w']:
            raise ValueError("Mode must be 'r', or 'w'")

        if self._mode == 'r' and not os.path.isfile(self._path):
            raise FileNotFoundError(f"No file found at {self._path}")

        if self._mode == 'w' and os.path.isfile(self._path):
            os.remove(self._path)

        self._file = open(self._path, self._mode)

    def read_line(self):
        if self._mode != 'r':
            raise Exception("File not opened in read mode.")
        line = next(self._file, None)
        if line:
            return line.strip()
        else:
            return None

    def write_line(self, line):
        if self._mode not in ['w']:
            raise Exception("File not opened in write mode.")
        self._file.write(line + '\n')

    def close_file(self):
        if self._file:
            self._file.close()
            self._file = None
            self._mode = None
