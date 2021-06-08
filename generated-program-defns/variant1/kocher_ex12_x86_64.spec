prog _generated_binaries_variant1_kocher_ex12_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__p_qword__r rbp - 0x10bv64, rsi;
    0x40000c: mov__r__p_qword rax, rbp - 8;
    0x400010: add__r__p_qword rax, rbp - 0x10bv64;
    0x400014: cmp__r__p_qword rax, 0x500000bv64;
    0x40001c: jae__w 0x400051bv64;
ENTRY_4194338:
    0x400022: mov__r__p_qword rax, rbp - 8;
    0x400026: add__r__p_qword rax, rbp - 0x10bv64;
    0x40002a: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x400032: shl__r__w ecx, 9;
    0x400035: movsxd__r__r rax, ecx;
    0x400038: movzx__r__p_byte ecx, rax + 0x500010bv64;
    0x400040: movzx__r__p_byte edx, 0x500018bv64;
    0x400048: and__r__r edx, ecx;
    0x40004a: mov__p_byte__r 0x500018bv64, dl;
    0x400051: pop__r rbp;
    0x400052: ret;
ENTRY_4194385:
    0x400051: pop__r rbp;
    0x400052: ret;
}
