prog _generated_binaries_variant1_kocher_ex12_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_qword__e rbp - 8, rdi;
    0x400008: mov__p_qword__e rbp - 0x10, rsi;
    0x40000c: mov__e__p_qword rax, rbp - 8;
    0x400010: add__e__p_qword rax, rbp - 0x10;
    0x400014: cmp__e__p_qword rax, 0x500000;
    0x40001c: jae__e 0x400051;
ENTRY_4194338:
    0x400022: mov__e__p_qword rax, rbp - 8;
    0x400026: add__e__p_qword rax, rbp - 0x10;
    0x40002a: movzx__e__p_byte ecx, rax + 0x500008;
    0x400032: shl__e__e ecx, 9;
    0x400035: movsxd__e__e rax, ecx;
    0x400038: movzx__e__p_byte ecx, rax + 0x500010;
    0x400040: movzx__e__p_byte edx, 0x500018;
    0x400048: and__e__e edx, ecx;
    0x40004a: mov__p_byte__e 0x500018, dl;
    0x400051: pop__e rbp;
    0x400052: ret;
ENTRY_4194385:
    0x400051: pop__e rbp;
    0x400052: ret;
}
