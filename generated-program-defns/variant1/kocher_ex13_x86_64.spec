prog _generated_binaries_variant1_kocher_ex13_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: sub__r__w rsp, 0x10bv64;
    0x400008: mov__p_qword__r rbp - 8, rdi;
    0x40000c: mov__r__p_qword rdi, rbp - 8;
    0x400010: call__w 0x500000bv64;
ENTRY_5242880:

ENTRY_4194325:
    0x400015: cmp__r__w eax, 0;
    0x400018: je__w 0x400049bv64;
ENTRY_4194377:
    0x400049: add__r__w rsp, 0x10bv64;
    0x40004d: pop__r rbp;
    0x40004e: ret;
ENTRY_4194334:
    0x40001e: mov__r__p_qword rax, rbp - 8;
    0x400022: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002a: shl__r__w ecx, 9;
    0x40002d: movsxd__r__r rax, ecx;
    0x400030: movzx__r__p_byte ecx, rax + 0x500010bv64;
    0x400038: movzx__r__p_byte edx, 0x500018bv64;
    0x400040: and__r__r edx, ecx;
    0x400042: mov__p_byte__r 0x500018bv64, dl;
    0x400049: add__r__w rsp, 0x10bv64;
    0x40004d: pop__r rbp;
    0x40004e: ret;
}
