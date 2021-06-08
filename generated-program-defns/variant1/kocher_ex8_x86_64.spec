prog _generated_binaries_variant1_kocher_ex8_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__r__p_qword rax, rbp - 8;
    0x40000cbv64: cmp__r__p_qword rax, 0x500000bv64;
    0x400014bv64: jae__w 0x40002dbv64;
ENTRY_4194330:
    0x40001abv64: mov__r__p_qword rax, rbp - 8;
    0x40001ebv64: add__r__w rax, 1;
    0x400024bv64: mov__p_qword__r rbp - 0x10bv64, rax;
    0x400028bv64: jmp__w 0x40003abv64;
ENTRY_4194349:
    0x40002dbv64: xor__r__r eax, eax;
    0x40002fbv64: mov__r__r ecx, eax;
    0x400031bv64: mov__p_qword__r rbp - 0x10bv64, rcx;
    0x400035bv64: jmp__w 0x40003abv64;
ENTRY_4194362:
    0x40003abv64: mov__r__p_qword rax, rbp - 0x10bv64;
    0x40003ebv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x400046bv64: shl__r__w ecx, 9;
    0x400049bv64: movsxd__r__r rax, ecx;
    0x40004cbv64: movzx__r__p_byte ecx, rax + 0x500010bv64;
    0x400054bv64: movzx__r__p_byte edx, 0x500018bv64;
    0x40005cbv64: and__r__r edx, ecx;
    0x40005ebv64: mov__p_byte__r 0x500018bv64, dl;
    0x400065bv64: pop__r rbp;
    0x400066bv64: ret;
}
