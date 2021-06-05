prog _generated_binaries_variant1_kocher_ex9_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_qword__e rbp - 8, rdi;
    0x400008: mov__p_qword__e rbp - 0x10, rsi;
    0x40000c: mov__e__p_qword rax, rbp - 0x10;
    0x400010: cmp__p_dword__e rax, 0;
    0x400013: je__e 0x400044;
ENTRY_4194372:
    0x400044: pop__e rbp;
    0x400045: ret;
ENTRY_4194329:
    0x400019: mov__e__p_qword rax, rbp - 8;
    0x40001d: movzx__e__p_byte ecx, rax + 0x500000;
    0x400025: shl__e__e ecx, 9;
    0x400028: movsxd__e__e rax, ecx;
    0x40002b: movzx__e__p_byte ecx, rax + 0x500008;
    0x400033: movzx__e__p_byte edx, 0x500010;
    0x40003b: and__e__e edx, ecx;
    0x40003d: mov__p_byte__e 0x500010, dl;
    0x400044: pop__e rbp;
    0x400045: ret;
}
