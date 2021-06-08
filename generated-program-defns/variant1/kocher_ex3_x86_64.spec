prog _generated_binaries_variant1_kocher_ex3_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: mov__p_byte__r rbp - 1, dil;
    0x400008bv64: movzx__r__p_byte eax, rbp - 1;
    0x40000cbv64: shl__r__w eax, 9;
    0x40000fbv64: movsxd__r__r rcx, eax;
    0x400012bv64: movzx__r__p_byte eax, rcx + 0x400001bv64;
    0x40001abv64: movzx__r__p_byte edx, 0x400001bv64;
    0x400022bv64: and__r__r edx, eax;
    0x400024bv64: mov__p_byte__r 0x400001bv64, dl;
    0x40002bbv64: pop__r rbp;
    0x40002cbv64: ret;
ENTRY_4194352:
    0x400030bv64: push__r rbp;
    0x400031bv64: mov__r__r rbp, rsp;
    0x400034bv64: sub__r__w rsp, 0x10bv64;
    0x400038bv64: mov__p_qword__r rbp - 8, rdi;
    0x40003cbv64: mov__r__p_qword rax, rbp - 8;
    0x400040bv64: cmp__r__p_qword rax, 0x400008bv64;
    0x400048bv64: jae__w 0x40005fbv64;
ENTRY_4194382:
    0x40004ebv64: mov__r__p_qword rax, rbp - 8;
    0x400052bv64: movzx__r__p_byte edi, rax + 0x400001bv64;
    0x40005abv64: call__w 0x400000bv64;
ENTRY_4194399:
    0x40005fbv64: add__r__w rsp, 0x10bv64;
    0x400063bv64: pop__r rbp;
    0x400064bv64: ret;
ENTRY_4194349:
    0x40002dbv64: nop__p_dword rax;
}
