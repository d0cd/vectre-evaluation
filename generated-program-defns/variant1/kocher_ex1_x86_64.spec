prog _generated_binaries_variant1_kocher_ex1_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__r__p_qword rax, rbp - 8;
    0x40000c: cmp__r__p_qword rax, 0x400008;
    0x400014: jae__w 0x400045;
ENTRY_4194384:
    0x400050: push__r rbp;
    0x400051: mov__r__r rbp, rsp;
    0x400054: pop__r rbp;
    0x400055: ret;
ENTRY_4194330:
    0x40001a: mov__r__p_qword rax, rbp - 8;
    0x40001e: movzx__r__p_byte ecx, rax + 0x400001;
    0x400026: shl__r__w ecx, 9;
    0x400029: movsxd__r__r rax, ecx;
    0x40002c: movzx__r__p_byte ecx, rax + 0x400001;
    0x400034: movzx__r__p_byte edx, 0x400001;
    0x40003c: and__r__r edx, ecx;
    0x40003e: mov__p_byte__r 0x400001, dl;
    0x400045: pop__r rbp;
    0x400046: ret;
ENTRY_4194373:
    0x400045: pop__r rbp;
    0x400046: ret;
ENTRY_4194375:
    0x400047: nop__p_word rax + rax;
}
