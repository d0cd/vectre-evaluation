prog _generated_binaries_variant1_kocher_ex10_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_qword__e rbp - 8, rdi;
    0x400008: mov__p_byte__e rbp - 9, sil;
    0x40000c: mov__e__p_qword rax, rbp - 8;
    0x400010: cmp__e__p_qword rax, 0x500000;
    0x400018: jae__e 0x400054;
ENTRY_4194334:
    0x40001e: mov__e__p_qword rax, rbp - 8;
    0x400022: movzx__e__p_byte ecx, rax + 0x500008;
    0x40002a: movzx__e__p_byte edx, rbp - 9;
    0x40002e: cmp__e__e ecx, edx;
    0x400030: jne__e 0x40004f;
ENTRY_4194388:
    0x400054: pop__e rbp;
    0x400055: ret;
ENTRY_4194358:
    0x400036: movzx__e__p_byte eax, 0x500010;
    0x40003e: movzx__e__p_byte ecx, 0x500018;
    0x400046: and__e__e ecx, eax;
    0x400048: mov__p_byte__e 0x500018, cl;
    0x40004f: jmp__e 0x400054;
ENTRY_4194383:
    0x40004f: jmp__e 0x400054;
}
