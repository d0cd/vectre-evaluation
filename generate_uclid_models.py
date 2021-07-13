#!/usr/bin/env python3

# This script does the following:
#   1. Clean all files and subdirectories in ./generated-program-defns
#   2. Attempt to generate a Vectre program definition for each piece of code in ./generated-binaries
#      while respecting the directory structure of ./generated-binaries

import os
import re
import shutil

uclid_dir = './generated-uclid'
prog_def_dir = './generated-program-defns'


def generate_uclid(root, name):
    if name == '.gitkeep': return
    file_path = os.path.join(root, name)
    new_path = file_path.replace(prog_def_dir, uclid_dir).replace(".spec", ".ucl")
    inst_def_path = _select_inst_def_path(file_path)
    plat_def_path = _select_plat_def_path(file_path)
    command = f"./vectre/vectre/target/debug/vectre {inst_def_path} {plat_def_path} {file_path} -s {new_path}"
    print(f"\n\nIssuing command: {command}")
    os.system(command)


def _select_inst_def_path(path):
    if 'variant1' in path:
        if 'aarch64' in path:
            return "inst-defns/aarch64_spectre_v1_instructions_complete.spec"
        elif 'x86_64' in path:
            return "inst-defns/x86_64_spectre_v1_instructions.spec"

    raise Exception(f"Can't find appropriate instruction definition file for path: {path}")


def _select_plat_def_path(path):
    if 'variant1' in path:
        if 'aarch64' in path:
            return "platform-defns/aarch64_spectre_v1_platform_complete.spec"
        elif 'x86_64' in path:
            return "platform-defns/aarch64_spectre_v1_platform_complete.spec"

    raise Exception(f"Can't find appropriate platform definition file for path: {path}")


if __name__ == '__main__':
    # Clean up generated uclid
    for file in os.listdir(uclid_dir):
        path = os.path.join(uclid_dir, file)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

    for root, dirs, files in os.walk(prog_def_dir):
        for name in files:
            generate_uclid(root, name)
        for name in dirs:
           dir_path = os.path.join(root, name)
           new_path = dir_path.replace(prog_def_dir, uclid_dir)
           if not os.path.exists(new_path):
               os.makedirs(new_path)
