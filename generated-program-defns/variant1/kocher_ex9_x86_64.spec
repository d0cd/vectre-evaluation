prog _generated_binaries_variant1_kocher_ex9_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__p_qword__r rbp - 0x10bv64, rsi;
    0x40000c: mov__r__p_qword rax, rbp - 0x10bv64;
    0x400010: cmp__p_dword__w rax, 0;
    0x400013: je__w 0x400044bv64;
ENTRY_4194372:
    0x400044: pop__r rbp;
    0x400045: ret;
ENTRY_4194329:
    0x400019: mov__r__p_qword rax, rbp - 8;
    0x40001d: movzx__r__p_byte ecx, rax + 0x500000bv64;
    0x400025: shl__r__w ecx, 9;
    0x400028: movsxd__r__r rax, ecx;
    0x40002b: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x400033: movzx__r__p_byte edx, 0x500010bv64;
    0x40003b: and__r__r edx, ecx;
    0x40003d: mov__p_byte__r 0x500010bv64, dl;
    0x400044: pop__r rbp;
    0x400045: ret;
}
