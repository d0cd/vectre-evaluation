prog _generated_binaries_variant1_kocher_ex1_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__r__p_qword rax, rbp - 8;
    0x40000cbv64: cmp__r__p_qword rax, 0x400008bv64;
    0x400014bv64: jae__w 0x400045bv64;
ENTRY_4194384:
    0x400050bv64: push__r rbp;
    0x400051bv64: mov__r__r rbp, rsp;
    0x400054bv64: pop__r rbp;
    0x400055bv64: ret;
ENTRY_4194330:
    0x40001abv64: mov__r__p_qword rax, rbp - 8;
    0x40001ebv64: movzx__r__p_byte ecx, rax + 0x400001bv64;
    0x400026bv64: shl__r__w ecx, 9;
    0x400029bv64: movsxd__r__r rax, ecx;
    0x40002cbv64: movzx__r__p_byte ecx, rax + 0x400001bv64;
    0x400034bv64: movzx__r__p_byte edx, 0x400001bv64;
    0x40003cbv64: and__r__r edx, ecx;
    0x40003ebv64: mov__p_byte__r 0x400001bv64, dl;
    0x400045bv64: pop__r rbp;
    0x400046bv64: ret;
ENTRY_4194373:
    0x400045bv64: pop__r rbp;
    0x400046bv64: ret;
ENTRY_4194375:
    0x400047bv64: nop__p_word rax + rax;
}
