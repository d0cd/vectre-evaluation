#!/usr/bin/env python3

# This script does the following:
#   1. Clean all files and subdirectories in ./generated-binaries
#   2. Attempt to generate an object file for each piece of code in ./program-source for each target architecture,
#      while respecting the directory structure of ./program-source

import os
import re
import shutil

bin_dir = './generated-binaries'
prog_dir = './program-source'
clang_targets = [
    'x86_64-unknown-linux-elf',
    'aarch64-unknown-linux-elf',
    'mips64-unknown-linux-elf'
]


def generate_objfiles(root, name):
    if name == '.gitkeep': return
    file_path = os.path.join(root, name)
    new_path = file_path.replace(prog_dir, bin_dir)
    for target in clang_targets:
        precise_path = new_path.replace(".c", f"_{target}.o".replace('-', '_'))
        if name == 'kocher_ex3.c':
            command = f"clang -c -fdeclspec -target {target} -o {precise_path} {file_path}"
        else:
            command = f"clang -c -target {target} -o {precise_path} {file_path}"
        print(f"\n\nIssuing command: {command}")
        os.system(command)


if __name__ == '__main__':
    # Clean  up generated binaries
    for file in os.listdir(bin_dir):
        path = os.path.join(bin_dir, file)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

    for root, dirs, files in os.walk(prog_dir):
        for name in files:
            generate_objfiles(root, name)
        for name in dirs:
           dir_path = os.path.join(root, name)
           new_path = dir_path.replace(prog_dir, bin_dir)
           if not os.path.exists(new_path):
               os.makedirs(new_path)
