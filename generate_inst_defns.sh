#!/bin/bash

rm ./inst-defns/aarch64_spectre_v1_instructions.spec
./vectre-angr-disasm/vectre-angr-disasm ./generated-binaries/variant1/*aarch64.o --inst-def ./inst-defns/aarch64_spectre_v1_instructions.spec

rm ./inst-defns/x86_64_spectre_v1_instructions.spec
./vectre-angr-disasm/vectre-angr-disasm ./generated-binaries/variant1/*x86_64.o --inst-def ./inst-defns/x86_64_spectre_v1_instructions.spec