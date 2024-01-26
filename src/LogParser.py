#!/usr/bin/env python3

import re


class LogParser:
    def __init__(self):
        self.log_regex = r'^(\d{2}-\d{2}-\d{4}-\d{2}:\d{2}:\d{2}\.\d{3})\s+(\w)/(\w+):\s+(.*)$'

    def parse(self, line):
        match = re.match(self.log_regex, line)
        if match:
            timestamp = match.group(1)
            log_level = match.group(2)
            tag = match.group(3)
            message = match.group(4)
            return {
                "timestamp": timestamp,
                "level": log_level,
                "tag": tag,
                "message": message
            }
        else:
            return None
