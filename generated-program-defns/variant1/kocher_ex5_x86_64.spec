prog _generated_binaries_variant1_kocher_ex5_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__r__p_qword rax, rbp - 8;
    0x40000c: cmp__r__p_qword rax, 0x500000;
    0x400014: jae__w 0x400076;
ENTRY_4194330:
    0x40001a: mov__r__p_qword rax, rbp - 8;
    0x40001e: sub__r__w rax, 1;
    0x400024: mov__p_qword__r rbp - 0x10, rax;
    0x400028: cmp__p_qword__w rbp - 0x10, 0;
    0x40002d: jb__w 0x400071;
ENTRY_4194422:
    0x400076: pop__r rbp;
    0x400077: ret;
ENTRY_4194417:
    0x400071: jmp__w 0x400076;
ENTRY_4194355:
    0x400033: mov__r__p_qword rax, rbp - 0x10;
    0x400037: movzx__r__p_byte ecx, rax + 0x500008;
    0x40003f: shl__r__w ecx, 9;
    0x400042: movsxd__r__r rax, ecx;
    0x400045: movzx__r__p_byte ecx, rax + 0x500010;
    0x40004d: movzx__r__p_byte edx, 0x500018;
    0x400055: and__r__r edx, ecx;
    0x400057: mov__p_byte__r 0x500018, dl;
    0x40005e: mov__r__p_qword rax, rbp - 0x10;
    0x400062: add__r__w rax, 1;
    0x400068: mov__p_qword__r rbp - 0x10, rax;
    0x40006c: jmp__w 0x400028;
ENTRY_4194344:
    0x400028: cmp__p_qword__w rbp - 0x10, 0;
    0x40002d: jb__w 0x400071;
}
