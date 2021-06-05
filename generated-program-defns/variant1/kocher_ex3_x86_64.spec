prog _generated_binaries_variant1_kocher_ex3_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_byte__e rbp - 1, dil;
    0x400008: movzx__e__p_byte eax, rbp - 1;
    0x40000c: shl__e__e eax, 9;
    0x40000f: movsxd__e__e rcx, eax;
    0x400012: movzx__e__p_byte eax, rcx + 0x400001;
    0x40001a: movzx__e__p_byte edx, 0x400001;
    0x400022: and__e__e edx, eax;
    0x400024: mov__p_byte__e 0x400001, dl;
    0x40002b: pop__e rbp;
    0x40002c: ret;
ENTRY_4194352:
    0x400030: push__e rbp;
    0x400031: mov__e__e rbp, rsp;
    0x400034: sub__e__e rsp, 0x10;
    0x400038: mov__p_qword__e rbp - 8, rdi;
    0x40003c: mov__e__p_qword rax, rbp - 8;
    0x400040: cmp__e__p_qword rax, 0x400008;
    0x400048: jae__e 0x40005f;
ENTRY_4194382:
    0x40004e: mov__e__p_qword rax, rbp - 8;
    0x400052: movzx__e__p_byte edi, rax + 0x400001;
    0x40005a: call__e 0x400000;
ENTRY_4194399:
    0x40005f: add__e__e rsp, 0x10;
    0x400063: pop__e rbp;
    0x400064: ret;
ENTRY_4194349:
    0x40002d: nop__p_dword rax;
}
