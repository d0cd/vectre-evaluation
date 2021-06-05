prog _generated_binaries_variant1_kocher_ex6_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: mov__p_qword__e rbp - 8, rdi;
    0x400008: mov__e__p_qword rax, rbp - 8;
    0x40000c: and__e__p_qword rax, 0x500000;
    0x400014: cmp__e__p_qword rax, rbp - 8;
    0x400018: jne__e 0x400049;
ENTRY_4194334:
    0x40001e: mov__e__p_qword rax, rbp - 8;
    0x400022: movzx__e__p_byte ecx, rax + 0x500008;
    0x40002a: shl__e__e ecx, 9;
    0x40002d: movsxd__e__e rax, ecx;
    0x400030: movzx__e__p_byte ecx, rax + 0x500010;
    0x400038: movzx__e__p_byte edx, 0x500018;
    0x400040: and__e__e edx, ecx;
    0x400042: mov__p_byte__e 0x500018, dl;
    0x400049: pop__e rbp;
    0x40004a: ret;
ENTRY_4194377:
    0x400049: pop__e rbp;
    0x40004a: ret;
}
