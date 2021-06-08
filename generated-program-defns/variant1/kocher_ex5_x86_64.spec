prog _generated_binaries_variant1_kocher_ex5_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__r__p_qword rax, rbp - 8;
    0x40000cbv64: cmp__r__p_qword rax, 0x500000bv64;
    0x400014bv64: jae__w 0x400076bv64;
ENTRY_4194330:
    0x40001abv64: mov__r__p_qword rax, rbp - 8;
    0x40001ebv64: sub__r__w rax, 1;
    0x400024bv64: mov__p_qword__r rbp - 0x10bv64, rax;
    0x400028bv64: cmp__p_qword__w rbp - 0x10bv64, 0;
    0x40002dbv64: jb__w 0x400071bv64;
ENTRY_4194422:
    0x400076bv64: pop__r rbp;
    0x400077bv64: ret;
ENTRY_4194417:
    0x400071bv64: jmp__w 0x400076bv64;
ENTRY_4194355:
    0x400033bv64: mov__r__p_qword rax, rbp - 0x10bv64;
    0x400037bv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40003fbv64: shl__r__w ecx, 9;
    0x400042bv64: movsxd__r__r rax, ecx;
    0x400045bv64: movzx__r__p_byte ecx, rax + 0x500010bv64;
    0x40004dbv64: movzx__r__p_byte edx, 0x500018bv64;
    0x400055bv64: and__r__r edx, ecx;
    0x400057bv64: mov__p_byte__r 0x500018bv64, dl;
    0x40005ebv64: mov__r__p_qword rax, rbp - 0x10bv64;
    0x400062bv64: add__r__w rax, 1;
    0x400068bv64: mov__p_qword__r rbp - 0x10bv64, rax;
    0x40006cbv64: jmp__w 0x400028bv64;
ENTRY_4194344:
    0x400028bv64: cmp__p_qword__w rbp - 0x10bv64, 0;
    0x40002dbv64: jb__w 0x400071bv64;
}
