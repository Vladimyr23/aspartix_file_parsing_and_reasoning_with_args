#!/usr/bin/env python
import re

class Apx_parser:
    def __init__(self, filepath):
        self.file = open(filepath, 'r')

    def read_file(self):
        arguments = []
        attacks = []
        #print("parser")
        lines = self.file.readlines()
        for line in lines:
            if line.startswith('arg'):
                arguments.append(re.search(r"\(([A-Za-z0-9]+)\)", line).group(1))
            elif line.startswith('att'):
                attacks.append(re.findall(r"\(([A-Za-z0-9,]+)\)", line))
            else:
                pass
        return arguments, attacks

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

