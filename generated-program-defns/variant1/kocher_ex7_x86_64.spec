prog _generated_binaries_variant1_kocher_ex7_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__r__p_qword rax, rbp - 8;
    0x40000cbv64: cmp__r__p_qword rax, 0x400068bv64;
    0x400014bv64: jne__w 0x400045bv64;
ENTRY_4194330:
    0x40001abv64: mov__r__p_qword rax, rbp - 8;
    0x40001ebv64: movzx__r__p_byte ecx, rax + 0x500000bv64;
    0x400026bv64: shl__r__w ecx, 9;
    0x400029bv64: movsxd__r__r rax, ecx;
    0x40002cbv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x400034bv64: movzx__r__p_byte edx, 0x500010bv64;
    0x40003cbv64: and__r__r edx, ecx;
    0x40003ebv64: mov__p_byte__r 0x500010bv64, dl;
    0x400045bv64: mov__r__p_qword rax, rbp - 8;
    0x400049bv64: cmp__r__p_qword rax, 0x500018bv64;
    0x400051bv64: jae__w 0x400063bv64;
ENTRY_4194373:
    0x400045bv64: mov__r__p_qword rax, rbp - 8;
    0x400049bv64: cmp__r__p_qword rax, 0x500018bv64;
    0x400051bv64: jae__w 0x400063bv64;
ENTRY_4194391:
    0x400057bv64: mov__r__p_qword rax, rbp - 8;
    0x40005bbv64: mov__p_qword__r 0x400068bv64, rax;
    0x400063bv64: pop__r rbp;
    0x400064bv64: ret;
ENTRY_4194403:
    0x400063bv64: pop__r rbp;
    0x400064bv64: ret;
}
