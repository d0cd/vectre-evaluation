prog _generated_binaries_variant1_kocher_ex10_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__p_byte__r rbp - 9, sil;
    0x40000cbv64: mov__r__p_qword rax, rbp - 8;
    0x400010bv64: cmp__r__p_qword rax, 0x500000bv64;
    0x400018bv64: jae__w 0x400054bv64;
ENTRY_4194334:
    0x40001ebv64: mov__r__p_qword rax, rbp - 8;
    0x400022bv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002abv64: movzx__r__p_byte edx, rbp - 9;
    0x40002ebv64: cmp__r__r ecx, edx;
    0x400030bv64: jne__w 0x40004fbv64;
ENTRY_4194388:
    0x400054bv64: pop__r rbp;
    0x400055bv64: ret;
ENTRY_4194358:
    0x400036bv64: movzx__r__p_byte eax, 0x500010bv64;
    0x40003ebv64: movzx__r__p_byte ecx, 0x500018bv64;
    0x400046bv64: and__r__r ecx, eax;
    0x400048bv64: mov__p_byte__r 0x500018bv64, cl;
    0x40004fbv64: jmp__w 0x400054bv64;
ENTRY_4194383:
    0x40004fbv64: jmp__w 0x400054bv64;
}
