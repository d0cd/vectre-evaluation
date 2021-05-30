#!/usr/bin/env python3

# This script does the following:
#   1. Clean all files and subdirectories in ./generated-binaries
#   2. Attempt to generate an object file for each piece of code in ./program-source for each target architecture,
#      while respecting the directory structure of ./program-source

import os
import shutil

from string import Template

bin_dir = './generated-binaries'
prog_dir = './program-source'
clang_targets = [
    'x86_64-unknown-linux-elf',
    'aarch64-unknown-linux-elf',
    'mips64-unknown-linux-elf'
]

compile_commands = {
    'kocher_ex3.c' : [
        ('x86_64', Template("clang -c -fdeclspec -target x86_64-unknown-linux-elf -o ${OUT_PATH} ${FILE_PATH}")),
        ('aarch64', Template("clang -c -fdeclspec -target aarch64-unknown-linux-elf -o ${OUT_PATH} ${FILE_PATH}")),
        ('mips64', Template("clang -c -fdeclspec -target mips64-unknown-linux-elf -o ${OUT_PATH} ${FILE_PATH}")),
        #('rv64', Template("riscv64-unknown-linux-gnu-gcc -c -o ${OUT_PATH} ${FILE_PATH}"))
    ],
    'default' :[
        ('x86_64', Template("clang -c -target x86_64-unknown-linux-elf -o ${OUT_PATH} ${FILE_PATH}")),
        ('aarch64', Template("clang -c -target aarch64-unknown-linux-elf -o ${OUT_PATH} ${FILE_PATH}")),
        ('mips64', Template("clang -c -target mips64-unknown-linux-elf -o ${OUT_PATH} ${FILE_PATH}")),
        ('rv64', Template("riscv64-unknown-linux-gnu-gcc -c -o ${OUT_PATH} ${FILE_PATH}"))
    ]
}


def generate_objfiles(root, name):
    if name == '.gitkeep': return
    file_path = os.path.join(root, name)
    new_path = file_path.replace(prog_dir, bin_dir)
    commands = compile_commands.get(name, compile_commands['default'])
    for (target, command) in commands:
        out_path = new_path.replace(".c", f"_{target}.o".replace('-', '_'))
        full_command = command.substitute(OUT_PATH=out_path, FILE_PATH=file_path)
        print(f"\n\nIssuing command: {full_command}")
        os.system(full_command)


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
