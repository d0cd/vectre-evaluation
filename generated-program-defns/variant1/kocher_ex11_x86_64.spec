prog _generated_binaries_variant1_kocher_ex11_x86_64 {
ENTRY_4194304:
    0x400000: push__e rbp;
    0x400001: mov__e__e rbp, rsp;
    0x400004: sub__e__e rsp, 0x10;
    0x400008: mov__p_qword__e rbp - 8, rdi;
    0x40000c: mov__e__p_qword rax, rbp - 8;
    0x400010: cmp__e__p_qword rax, 0x500000;
    0x400018: jae__e 0x400059;
ENTRY_4194334:
    0x40001e: mov__e__p_qword rax, rbp - 8;
    0x400022: movzx__e__p_byte ecx, rax + 0x500008;
    0x40002a: shl__e__e ecx, 9;
    0x40002d: movsxd__e__e rax, ecx;
    0x400030: movabs__e__e rdx, 0x500010;
    0x40003a: add__e__e rdx, rax;
    0x40003d: mov__e__e edi, 0x500018;
    0x400042: mov__e__e eax, 1;
    0x400047: mov__e__e rsi, rdx;
    0x40004a: mov__e__e rdx, rax;
    0x40004d: call__e 0x500020;
ENTRY_4194393:
    0x400059: add__e__e rsp, 0x10;
    0x40005d: pop__e rbp;
    0x40005e: ret;
ENTRY_5242912:

ENTRY_4194386:
    0x400052: mov__p_byte__e 0x500018, al;
    0x400059: add__e__e rsp, 0x10;
    0x40005d: pop__e rbp;
    0x40005e: ret;
}
