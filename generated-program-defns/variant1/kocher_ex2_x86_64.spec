prog _generated_binaries_variant1_kocher_ex2_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_byte__r rbp - 1, dil;
    0x400008: movzx__r__p_byte eax, rbp - 1;
    0x40000c: shl__r__w eax, 9;
    0x40000f: movsxd__r__r rcx, eax;
    0x400012: movzx__r__p_byte eax, rcx + 0x500000;
    0x40001a: movzx__r__p_byte edx, 0x500008;
    0x400022: and__r__r edx, eax;
    0x400024: mov__p_byte__r 0x500008, dl;
    0x40002b: pop__r rbp;
    0x40002c: ret;
ENTRY_4194352:
    0x400030: push__r rbp;
    0x400031: mov__r__r rbp, rsp;
    0x400034: sub__r__w rsp, 0x10;
    0x400038: mov__p_qword__r rbp - 8, rdi;
    0x40003c: mov__r__p_qword rax, rbp - 8;
    0x400040: cmp__r__p_qword rax, 0x500010;
    0x400048: jae__w 0x400061;
ENTRY_4194382:
    0x40004e: mov__r__p_qword rax, rbp - 8;
    0x400052: movzx__r__p_byte edi, rax + 0x500018;
    0x40005a: mov__r__w al, 0;
    0x40005c: call__w 0x500020;
ENTRY_4194401:
    0x400061: add__r__w rsp, 0x10;
    0x400065: pop__r rbp;
    0x400066: ret;
ENTRY_5242912:

ENTRY_4194349:
    0x40002d: nop__p_dword rax;
}
