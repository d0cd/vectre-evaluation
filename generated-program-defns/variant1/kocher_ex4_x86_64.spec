prog _generated_binaries_variant1_kocher_ex4_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__r__p_qword rax, rbp - 8;
    0x40000cbv64: cmp__r__p_qword rax, 0x500000bv64;
    0x400014bv64: jae__w 0x400049bv64;
ENTRY_4194330:
    0x40001abv64: mov__r__p_qword rax, rbp - 8;
    0x40001ebv64: shl__r__w rax, 1;
    0x400022bv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002abv64: shl__r__w ecx, 9;
    0x40002dbv64: movsxd__r__r rax, ecx;
    0x400030bv64: movzx__r__p_byte ecx, rax + 0x500010bv64;
    0x400038bv64: movzx__r__p_byte edx, 0x500018bv64;
    0x400040bv64: and__r__r edx, ecx;
    0x400042bv64: mov__p_byte__r 0x500018bv64, dl;
    0x400049bv64: pop__r rbp;
    0x40004abv64: ret;
ENTRY_4194377:
    0x400049bv64: pop__r rbp;
    0x40004abv64: ret;
}
