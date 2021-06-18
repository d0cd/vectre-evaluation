#!/bin/bash

rm ./platform-defns/aarch64_spectre_v1_platform_complete.spec
./vectre-angr-disasm/vectre-angr-disasm ./generated-binaries/variant1/*aarch64.o --plat-def ./platform-defns/aarch64_spectre_v1_platform_complete.spec

rm ./platform-defns/x86_64_spectre_v1_platform.spec
./vectre-angr-disasm/vectre-angr-disasm ./generated-binaries/variant1/*x86_64.o --plat-def ./platform-defns/x86_64_spectre_v1_platform.spec