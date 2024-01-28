# Tars LogReader

![image info](res/tars.jpeg)

## Introduction

LogReader is a Python tool designed to parse, filter, and output log files based on specific tags, messages, and other
parameters. It can handle both individual log files and directories containing multiple logs. This tool is designed to
be compatible with the [FileLogger](https://github.com/aabolfazl/FileLogger) library.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/aabolfazl/Tars.git
cd LogReader
```

Ensure you have Python installed on your system. LogReader is compatible with Python 3.

## Usage

To use LogReader, run the `Log_reader.py` script with Python, providing the necessary arguments.

### Basic Command

```bash
python logreader.py -i <input_path> [other options]
```

### Arguments

- `-i`, `--input`: The input file or directory path. (Required)
- `-t`, `--tags`: A list of tags for filtering log entries.
- `-m`, `--messages`: A list of messages for filtering log entries.
- `-o`, `--output`: The output file path. If not provided, the output will be named with the current timestamp.
- `-e`, `--exception`: Flag to show exceptions.

### Examples

**Example 1:** Parse a single log file and filter by tags.

```bash
python Log_reader.py -i /path/to/logfile.log -t ERROR WARNING
```

**Example 2:** Parse all logs in a directory and filter by specific messages, outputting to a specified file.

```bash
python Log_reader.py -i /path/to/logs/ -m "OutOfMemoryError" "NullPointerException" -o /path/to/output.txt
```

**Example 3:** Handle a single log file and show exceptions in the output.

```bash
python Log_reader.py -i /path/to/logfile.log -e True
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

