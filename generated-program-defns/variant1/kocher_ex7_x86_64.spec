prog _generated_binaries_variant1_kocher_ex7_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__r__p_qword rax, rbp - 8;
    0x40000c: cmp__r__p_qword rax, 0x400068bv64;
    0x400014: jne__w 0x400045bv64;
ENTRY_4194330:
    0x40001a: mov__r__p_qword rax, rbp - 8;
    0x40001e: movzx__r__p_byte ecx, rax + 0x500000bv64;
    0x400026: shl__r__w ecx, 9;
    0x400029: movsxd__r__r rax, ecx;
    0x40002c: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x400034: movzx__r__p_byte edx, 0x500010bv64;
    0x40003c: and__r__r edx, ecx;
    0x40003e: mov__p_byte__r 0x500010bv64, dl;
    0x400045: mov__r__p_qword rax, rbp - 8;
    0x400049: cmp__r__p_qword rax, 0x500018bv64;
    0x400051: jae__w 0x400063bv64;
ENTRY_4194373:
    0x400045: mov__r__p_qword rax, rbp - 8;
    0x400049: cmp__r__p_qword rax, 0x500018bv64;
    0x400051: jae__w 0x400063bv64;
ENTRY_4194391:
    0x400057: mov__r__p_qword rax, rbp - 8;
    0x40005b: mov__p_qword__r 0x400068bv64, rax;
    0x400063: pop__r rbp;
    0x400064: ret;
ENTRY_4194403:
    0x400063: pop__r rbp;
    0x400064: ret;
}
