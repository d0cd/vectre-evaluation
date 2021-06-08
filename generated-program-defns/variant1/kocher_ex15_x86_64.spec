prog _generated_binaries_variant1_kocher_ex15_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_qword__r rbp - 8, rdi;
    0x400008bv64: mov__r__p_qword rax, rbp - 8;
    0x40000cbv64: mov__r__p_qword rax, rax;
    0x40000fbv64: cmp__r__p_qword rax, 0x500000bv64;
    0x400017bv64: jae__w 0x40004bbv64;
ENTRY_4194333:
    0x40001dbv64: mov__r__p_qword rax, rbp - 8;
    0x400021bv64: mov__r__p_qword rax, rax;
    0x400024bv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002cbv64: shl__r__w ecx, 9;
    0x40002fbv64: movsxd__r__r rax, ecx;
    0x400032bv64: movzx__r__p_byte ecx, rax + 0x500010bv64;
    0x40003abv64: movzx__r__p_byte edx, 0x500018bv64;
    0x400042bv64: and__r__r edx, ecx;
    0x400044bv64: mov__p_byte__r 0x500018bv64, dl;
    0x40004bbv64: pop__r rbp;
    0x40004cbv64: ret;
ENTRY_4194379:
    0x40004bbv64: pop__r rbp;
    0x40004cbv64: ret;
}
