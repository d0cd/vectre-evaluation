prog _generated_binaries_variant1_kocher_ex9_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__p_qword__r rbp - 0x10bv64, rsi;
    0x40000cbv64: mov__r__p_qword rax, rbp - 0x10bv64;
    0x400010bv64: cmp__p_dword__w rax, 0;
    0x400013bv64: je__w 0x400044bv64;
ENTRY_4194372:
    0x400044bv64: pop__r rbp;
    0x400045bv64: ret;
ENTRY_4194329:
    0x400019bv64: mov__r__p_qword rax, rbp - 8;
    0x40001dbv64: movzx__r__p_byte ecx, rax + 0x500000bv64;
    0x400025bv64: shl__r__w ecx, 9;
    0x400028bv64: movsxd__r__r rax, ecx;
    0x40002bbv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x400033bv64: movzx__r__p_byte edx, 0x500010bv64;
    0x40003bbv64: and__r__r edx, ecx;
    0x40003dbv64: mov__p_byte__r 0x500010bv64, dl;
    0x400044bv64: pop__r rbp;
    0x400045bv64: ret;
}
