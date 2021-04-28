# vectre-evaluation
Evaluation source code for the Vectre++ tool.

## Project Structure
`program-source` - Contains source code for vulnerable/safe programs.

`generated-binaries` - Contains RISCV binaries corresponding to those in `program-source`. Automatically generated.

`generated-program-defns` - Contains program definitions compatible with Vectre, corresponding to those in `program-source`. Automatically generated.

`generated-uclid` - Contains UCLID5 verification tasks corresponding to those in `generated-program-defns`. Automatically generated.

`edited-program-defns` - Contains customized program definitions for specific verification tasks. Manually edited.

`edited-uclid` - Contains customized UCLID5 code for specific verification tasks. Automatically generated or manually edited.

## Usage
1. Use scripts to build and run complete verification pipelines for benchmarks in `program-source`.
2. Customize desired verification tasks by modifying program definitions or generated UCLID5 code.

- Do not manually edit stuff in the `generated-*` subdirectories. These will likely be overwritten.
- If you would like to manually experiment, maintain your code in the `edited-*` subdirectories.
