#!/usr/bin/env python3
import argparse
import re
import os
import sys


class ArgParser:
    def __init__(self, args):
        self.args_parser = argparse.ArgumentParser(description='Creates a file that contains all the errors from '
                                                               'the logs. Using: script.py --file file_with_logs '
                                                               'extension doesn\'t matter')

        self.args_parser.add_argument('--file', dest='log_file', required=False,
                                      help='sample: --file messages.1')
        self.args_parser.add_argument('--out', dest='out_file', default='logs.txt', type=str, required=False,
                                      help='Optionally, the name of the output file, the file will be created in the'
                                           ' current directory,'
                                           ' default: logs.txt, sample: --out logs.txt')
        self.args_parser.add_argument('--remove_double', dest='double_flag', action='store_true',
                                      help='Removes identical errors from the output file default: False')
        self.args_parser.add_argument('--all', dest='read_all_flag', action='store_true',
                                      help='Processing all files with logs in the current directory, '
                                           'no --file argument required, default: False')

        self._args = self.args_parser.parse_args(args)
        self.log_file = self._args.log_file
        self.out_file = self._args.out_file
        self.double_flag = self._args.double_flag
        self.read_all_flag = self._args.read_all_flag


def find_errors(lines, str_type_of_error, remove_double):
    seen = set()
    res = []
    pattern = re.compile(re.escape(str_type_of_error))
    for line in lines:
        result = pattern.search(line)
        if result is not None:
            if remove_double:
                error = re.search(r']: .*[a-zA-z]:', line)
                if error:
                    error = error.group(0)
                if error not in seen:
                    res.append(line)
                    seen.add(error)
            else:
                res.append(line)
    return res


def read_all(out_file):
    text = []
    files = os.listdir(os.getcwd())
    for filename in files:
        if not filename.endswith('.py') and filename != out_file:
            with open(filename, 'r') as f:
                text += f.readlines()
    return text


def main():
    args = ArgParser(sys.argv[1:])
    log_file = args.log_file
    out_file = args.out_file
    double_flag = args.double_flag
    read_all_flag = args.read_all_flag
    result = []
    types_of_error = ['[ERROR]','failed']
    if read_all_flag:
        lines = read_all(out_file)
    else:
        with open(log_file) as f:
            lines = f.readlines()
    for error in types_of_error:
        result += find_errors(lines, error, double_flag)
    with open(out_file, 'a+') as f:
        for str in result:
            f.write(str)


if __name__ == '__main__':
    main()
