prog _generated_binaries_variant1_kocher_ex15_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_qword__e rbp - 8, rdi;
    0x400008: mov__e__p_qword rax, rbp - 8;
    0x40000c: mov__e__p_qword rax, rax;
    0x40000f: cmp__e__p_qword rax, 0x500000;
    0x400017: jae__e 0x40004b;
ENTRY_4194333:
    0x40001d: mov__e__p_qword rax, rbp - 8;
    0x400021: mov__e__p_qword rax, rax;
    0x400024: movzx__e__p_byte ecx, rax + 0x500008;
    0x40002c: shl__e__e ecx, 9;
    0x40002f: movsxd__e__e rax, ecx;
    0x400032: movzx__e__p_byte ecx, rax + 0x500010;
    0x40003a: movzx__e__p_byte edx, 0x500018;
    0x400042: and__e__e edx, ecx;
    0x400044: mov__p_byte__e 0x500018, dl;
    0x40004b: pop__e rbp;
    0x40004c: ret;
ENTRY_4194379:
    0x40004b: pop__e rbp;
    0x40004c: ret;
}
