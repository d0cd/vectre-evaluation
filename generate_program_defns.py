#!/usr/bin/env python3

# This script does the following:
#   1. Clean all files and subdirectories in ./generated-program-defns
#   2. Attempt to generate a Vectre program definition for each piece of code in ./generated-binaries
#      while respecting the directory structure of ./generated-binaries

import os
import re
import shutil

prog_def_dir = './generated-program-defns'
bin_dir = './generated-binaries'


def generate_objfiles(root, name):
    if name == '.gitkeep': return
    file_path = os.path.join(root, name)
    new_path = file_path.replace(bin_dir, prog_def_dir).replace(".o", ".spec")
    command = f"./vectre-angr-disasm/vectre-angr-disasm {file_path} {new_path}"
    print(f"\n\nIssuing command: {command}")
    os.system(command)


if __name__ == '__main__':
    # Clean  up generated binaries
    for file in os.listdir(prog_def_dir):
        path = os.path.join(prog_def_dir, file)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

    for root, dirs, files in os.walk(bin_dir):
        for name in files:
            generate_objfiles(root, name)
        for name in dirs:
           dir_path = os.path.join(root, name)
           new_path = dir_path.replace(bin_dir, prog_def_dir)
           if not os.path.exists(new_path):
               os.makedirs(new_path)
