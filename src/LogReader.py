#!/usr/bin/env python3

from FileHandler import FileHandler
from LogParser import LogParser


class LogReader:
    def __init__(self, args):
        print(args)
        self._args = args
        self._tags = set()
        self._output_file = args.output_file
        self._input_file = args.input_file
        self.set_tags(args)

    def set_tags(self, args):
        if args.tags:
            for tag in args.tags:
                self._tags.add(tag)

    def start(self):
        parser = LogParser()
        file_reader = FileHandler(self._input_file, 'r')
        file_reader.open_file()
        line_count = 0

        if self._output_file:
            file_writer = FileHandler(self._output_file, 'w')
            file_writer.open_file()
        else:
            file_writer = None

        while True:
            line = file_reader.read_line()
            if line is None:
                break

            line_count += 1
            parsed_line = parser.parse(line)

            if parsed_line is not None and parsed_line["tag"] in self._tags:
                if file_writer:
                    file_writer.write_line(line)
                else:
                    print(line)

        file_reader.close_file()
        if file_writer:
            file_writer.close_file()

        print(f"Done, {line_count} Read")
