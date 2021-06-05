prog _generated_binaries_variant1_kocher_ex8_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_qword__e rbp - 8, rdi;
    0x400008: mov__e__p_qword rax, rbp - 8;
    0x40000c: cmp__e__p_qword rax, 0x500000;
    0x400014: jae__e 0x40002d;
ENTRY_4194330:
    0x40001a: mov__e__p_qword rax, rbp - 8;
    0x40001e: add__e__e rax, 1;
    0x400024: mov__p_qword__e rbp - 0x10, rax;
    0x400028: jmp__e 0x40003a;
ENTRY_4194349:
    0x40002d: xor__e__e eax, eax;
    0x40002f: mov__e__e ecx, eax;
    0x400031: mov__p_qword__e rbp - 0x10, rcx;
    0x400035: jmp__e 0x40003a;
ENTRY_4194362:
    0x40003a: mov__e__p_qword rax, rbp - 0x10;
    0x40003e: movzx__e__p_byte ecx, rax + 0x500008;
    0x400046: shl__e__e ecx, 9;
    0x400049: movsxd__e__e rax, ecx;
    0x40004c: movzx__e__p_byte ecx, rax + 0x500010;
    0x400054: movzx__e__p_byte edx, 0x500018;
    0x40005c: and__e__e edx, ecx;
    0x40005e: mov__p_byte__e 0x500018, dl;
    0x400065: pop__e rbp;
    0x400066: ret;
}
