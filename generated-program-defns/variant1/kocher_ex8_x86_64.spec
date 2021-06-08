prog _generated_binaries_variant1_kocher_ex8_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__r__p_qword rax, rbp - 8;
    0x40000c: cmp__r__p_qword rax, 0x500000;
    0x400014: jae__w 0x40002d;
ENTRY_4194330:
    0x40001a: mov__r__p_qword rax, rbp - 8;
    0x40001e: add__r__w rax, 1;
    0x400024: mov__p_qword__r rbp - 0x10, rax;
    0x400028: jmp__w 0x40003a;
ENTRY_4194349:
    0x40002d: xor__r__r eax, eax;
    0x40002f: mov__r__r ecx, eax;
    0x400031: mov__p_qword__r rbp - 0x10, rcx;
    0x400035: jmp__w 0x40003a;
ENTRY_4194362:
    0x40003a: mov__r__p_qword rax, rbp - 0x10;
    0x40003e: movzx__r__p_byte ecx, rax + 0x500008;
    0x400046: shl__r__w ecx, 9;
    0x400049: movsxd__r__r rax, ecx;
    0x40004c: movzx__r__p_byte ecx, rax + 0x500010;
    0x400054: movzx__r__p_byte edx, 0x500018;
    0x40005c: and__r__r edx, ecx;
    0x40005e: mov__p_byte__r 0x500018, dl;
    0x400065: pop__r rbp;
    0x400066: ret;
}
