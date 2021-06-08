prog _generated_binaries_variant1_kocher_ex10_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__p_byte__r rbp - 9, sil;
    0x40000c: mov__r__p_qword rax, rbp - 8;
    0x400010: cmp__r__p_qword rax, 0x500000bv64;
    0x400018: jae__w 0x400054bv64;
ENTRY_4194334:
    0x40001e: mov__r__p_qword rax, rbp - 8;
    0x400022: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002a: movzx__r__p_byte edx, rbp - 9;
    0x40002e: cmp__r__r ecx, edx;
    0x400030: jne__w 0x40004fbv64;
ENTRY_4194388:
    0x400054: pop__r rbp;
    0x400055: ret;
ENTRY_4194358:
    0x400036: movzx__r__p_byte eax, 0x500010bv64;
    0x40003e: movzx__r__p_byte ecx, 0x500018bv64;
    0x400046: and__r__r ecx, eax;
    0x400048: mov__p_byte__r 0x500018bv64, cl;
    0x40004f: jmp__w 0x400054bv64;
ENTRY_4194383:
    0x40004f: jmp__w 0x400054bv64;
}
