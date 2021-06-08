prog _generated_binaries_variant1_kocher_ex14_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__r__p_qword rax, rbp - 8;
    0x40000c: cmp__r__p_qword rax, 0x500000;
    0x400014: jae__w 0x40004b;
ENTRY_4194330:
    0x40001a: mov__r__p_qword rax, rbp - 8;
    0x40001e: xor__r__w rax, 0xff;
    0x400024: movzx__r__p_byte ecx, rax + 0x500008;
    0x40002c: shl__r__w ecx, 9;
    0x40002f: movsxd__r__r rax, ecx;
    0x400032: movzx__r__p_byte ecx, rax + 0x500010;
    0x40003a: movzx__r__p_byte edx, 0x500018;
    0x400042: and__r__r edx, ecx;
    0x400044: mov__p_byte__r 0x500018, dl;
    0x40004b: pop__r rbp;
    0x40004c: ret;
ENTRY_4194379:
    0x40004b: pop__r rbp;
    0x40004c: ret;
}
