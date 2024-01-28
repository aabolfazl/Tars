#!/usr/bin/env python3
import datetime
import os

from FileHandler import FileHandler
from LogParser import LogParser


class LogReader:
    def __init__(self, args):
        print(args)
        self._tags = set()
        self._messages = set()
        self._log_file = args.input
        self._line_count = 0
        self._show_exception = args.exception
        self._parser = LogParser()

        if args.output:
            self._output = args.output
        else:
            self._output = os.path.join(self._log_file, f"tmp.txt")

        self.set_tags(args)
        self.set_messages(args)

    def set_tags(self, args):
        if args.tags:
            for tag in args.tags:
                self._tags.add(tag)

    def set_messages(self, args):
        if args.messages:
            for message in args.messages:
                self._messages.add(message)

    def start(self):
        is_directory = os.path.isdir(self._log_file)

        output_handler = FileHandler(self._output, 'w')
        output_handler.open_file()

        if is_directory:
            all_files = os.listdir(self._log_file)
            sorted_files = sorted(all_files)

            for filename in sorted_files:
                if filename.startswith("tmp"):
                    continue

                file_path = os.path.join(self._log_file, filename)
                if os.path.isfile(file_path):
                    output_handler.write_line("\n\nstart of file: " + file_path)
                    self.start_single(file_path, output_handler)
        else:
            self.start_single(self._log_file, output_handler)

        if output_handler:
            output_handler.close_file()
            current_time = datetime.datetime.now().strftime("%d_%m_%Y_%H:%M:%S")
            new_file_path = os.path.join(os.path.dirname(self._output), f"logs_{current_time}.txt")
            os.rename(self._output, new_file_path)

        print(f"Done, {self._line_count} Read")

    def start_single(self, file_path, output_handler):
        file_reader = FileHandler(file_path, 'r')
        file_reader.open_file()

        while True:
            line = file_reader.read_line()
            if line is None:
                break

            if not self._tags and not self._messages:
                break

            self._line_count += 1
            parsed_line = self._parser.parse(line)

            if parsed_line is not None:
                tag = parsed_line['tag']
                message = parsed_line['message']

                should_write = tag in self._tags or self.contain_messages(message) or self.show_exception(tag, message)

                if should_write:
                    output_handler.write_line(line)

        file_reader.close_file()

    def contain_messages(self, read) -> bool:
        for message in self._messages:
            if message in read:
                return True
        return False

    def show_exception(self, tag, message) -> bool:
        return self._show_exception and tag == "E" or self._show_exception and "Exception" in message
