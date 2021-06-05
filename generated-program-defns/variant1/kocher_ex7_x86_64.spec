prog _generated_binaries_variant1_kocher_ex7_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_qword__e rbp - 8, rdi;
    0x400008: mov__e__p_qword rax, rbp - 8;
    0x40000c: cmp__e__p_qword rax, 0x400068;
    0x400014: jne__e 0x400045;
ENTRY_4194330:
    0x40001a: mov__e__p_qword rax, rbp - 8;
    0x40001e: movzx__e__p_byte ecx, rax + 0x500000;
    0x400026: shl__e__e ecx, 9;
    0x400029: movsxd__e__e rax, ecx;
    0x40002c: movzx__e__p_byte ecx, rax + 0x500008;
    0x400034: movzx__e__p_byte edx, 0x500010;
    0x40003c: and__e__e edx, ecx;
    0x40003e: mov__p_byte__e 0x500010, dl;
    0x400045: mov__e__p_qword rax, rbp - 8;
    0x400049: cmp__e__p_qword rax, 0x500018;
    0x400051: jae__e 0x400063;
ENTRY_4194373:
    0x400045: mov__e__p_qword rax, rbp - 8;
    0x400049: cmp__e__p_qword rax, 0x500018;
    0x400051: jae__e 0x400063;
ENTRY_4194391:
    0x400057: mov__e__p_qword rax, rbp - 8;
    0x40005b: mov__p_qword__e 0x400068, rax;
    0x400063: pop__e rbp;
    0x400064: ret;
ENTRY_4194403:
    0x400063: pop__e rbp;
    0x400064: ret;
}
