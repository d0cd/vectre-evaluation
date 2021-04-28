import argparse
import os
import shutil

from pathlib import Path
from verification_options import *

if '__name__' == '__main__':
    parser = argparse.ArgumentParser(description="Driver for Vectre verification tasks.")
    parser.add_argument('path_to_prog_defns', metavar='PATH', nargs=1, type=str,
                        help='Path to program definition for verification.')
    parser.add_argument('output_dir', metavar='DIR', nargs=1, type=str,
                        help='Path to output directory to store verification results.')
    parser.add_argument('attack', metavar='ATK', nargs=1, type=str,
                        help='Selected transient execution attack.')
    parser.add_argument('--isa', metavar='ISA', nargs=1, default='RV64', type=str,
                        help='Instruction Set Architecture used by the binary.')
    parser.add_argument('--spec_depth', metavar='N', nargs=1, default=4, type=int,
                        help='Maximum speculation depth of the models.')
    parser.add_argument('--bmc_depth', metavar='N', nargs=1, default=10, type=int,
                        help='Maximum number of basic blocks to execute.')
    parser.add_argument('--no_compile_src', action='store_true')
    parser.add_argument('--no_compile_queries', action='store_true')
    parser.add_argument('--no_exec', action='store_true')
    args = parser.parse_args()

    assert isa_is_valid(args.isa), f"Invalid ISA: {args.isa}"
    assert attack_is_valid(args.attack), f"Invalid attack: {args.attack}"
    assert(os.path.isdir(args.output_dir), f"Directory: {args.output_dir} does not exist.")

    prog_defn_name = Path(args.path_to_prog_defns).resolve().stem

    if not args.no_compile_src:
        # If `vectre_gen_src_{binary_name}_{attack}/` exists, delete it
        # Create the directory again
        src_path = os.path.join(args.output_dir, f"vectre_gen_src_{binary_name}_{args.attack}")
        if os.path.exists(src_path):
            shutil.rmtree(src_path)
        os.makedirs(src_path)

        
        # Disassemble binary and store in source directory


        # Compile and store platform model in source directory

    if not args.no_compile_queries:
        # If `vectre_gen_queries_{binary_name}_{attack}/` exists, delete it
        # Create the directory again
        query_path = os.path.join(args.output_dir, f"vectre_gen_queries_{binary_name}_{args.attack}")
        if os.path.exists(query_path):
            shutil.rmtree(query_path)
        os.makedirs(query_path)

        for i in range(args.spec_depth):
            for j in range(args.bmc_depth):
                # Create directories for each query and populate them
                pass

    if not args.no_exec:
        # Now execute the queries and store results
        pass


    


