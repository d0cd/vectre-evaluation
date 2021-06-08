prog _generated_binaries_variant1_kocher_ex11_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: sub__r__w rsp, 0x10bv64;
    0x400008: mov__p_qword__r rbp - 8, rdi;
    0x40000c: mov__r__p_qword rax, rbp - 8;
    0x400010: cmp__r__p_qword rax, 0x500000bv64;
    0x400018: jae__w 0x400059bv64;
ENTRY_4194334:
    0x40001e: mov__r__p_qword rax, rbp - 8;
    0x400022: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002a: shl__r__w ecx, 9;
    0x40002d: movsxd__r__r rax, ecx;
    0x400030: movabs__r__w rdx, 0x500010bv64;
    0x40003a: add__r__r rdx, rax;
    0x40003d: mov__r__w edi, 0x500018bv64;
    0x400042: mov__r__w eax, 1;
    0x400047: mov__r__r rsi, rdx;
    0x40004a: mov__r__r rdx, rax;
    0x40004d: call__w 0x500020bv64;
ENTRY_4194393:
    0x400059: add__r__w rsp, 0x10bv64;
    0x40005d: pop__r rbp;
    0x40005e: ret;
ENTRY_5242912:

ENTRY_4194386:
    0x400052: mov__p_byte__r 0x500018bv64, al;
    0x400059: add__r__w rsp, 0x10bv64;
    0x40005d: pop__r rbp;
    0x40005e: ret;
}
