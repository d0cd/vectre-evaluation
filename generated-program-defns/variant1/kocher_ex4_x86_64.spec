prog _generated_binaries_variant1_kocher_ex4_x86_64 {
ENTRY_4194304:
    0x400000: push__r rbp;
    0x400001: mov__r__r rbp, rsp;
    0x400004: mov__p_qword__r rbp - 8, rdi;
    0x400008: mov__r__p_qword rax, rbp - 8;
    0x40000c: cmp__r__p_qword rax, 0x500000bv64;
    0x400014: jae__w 0x400049bv64;
ENTRY_4194330:
    0x40001a: mov__r__p_qword rax, rbp - 8;
    0x40001e: shl__r__w rax, 1;
    0x400022: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002a: shl__r__w ecx, 9;
    0x40002d: movsxd__r__r rax, ecx;
    0x400030: movzx__r__p_byte ecx, rax + 0x500010bv64;
    0x400038: movzx__r__p_byte edx, 0x500018bv64;
    0x400040: and__r__r edx, ecx;
    0x400042: mov__p_byte__r 0x500018bv64, dl;
    0x400049: pop__r rbp;
    0x40004a: ret;
ENTRY_4194377:
    0x400049: pop__r rbp;
    0x40004a: ret;
}
