prog _generated_binaries_variant1_kocher_ex13_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: sub__e__e rsp, 0x10;
    0x400008: mov__p_qword__e rbp - 8, rdi;
    0x40000c: mov__e__p_qword rdi, rbp - 8;
    0x400010: call__e 0x500000;
ENTRY_5242880:

ENTRY_4194325:
    0x400015: cmp__e__e eax, 0;
    0x400018: je__e 0x400049;
ENTRY_4194377:
    0x400049: add__e__e rsp, 0x10;
    0x40004d: pop__e rbp;
    0x40004e: ret;
ENTRY_4194334:
    0x40001e: mov__e__p_qword rax, rbp - 8;
    0x400022: movzx__e__p_byte ecx, rax + 0x500008;
    0x40002a: shl__e__e ecx, 9;
    0x40002d: movsxd__e__e rax, ecx;
    0x400030: movzx__e__p_byte ecx, rax + 0x500010;
    0x400038: movzx__e__p_byte edx, 0x500018;
    0x400040: and__e__e edx, ecx;
    0x400042: mov__p_byte__e 0x500018, dl;
    0x400049: add__e__e rsp, 0x10;
    0x40004d: pop__e rbp;
    0x40004e: ret;
}
