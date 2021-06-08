prog _generated_binaries_variant1_kocher_ex11_x86_64 {
ENTRY_4194304:
    0x400000bv64: push__r rbp;
    0x400001bv64: mov__r__r rbp, rsp;
    0x400004bv64: sub__r__w rsp, 0x10bv64;
    0x400008bv64: mov__p_qword__r rbp - 8, rdi;
    0x40000cbv64: mov__r__p_qword rax, rbp - 8;
    0x400010bv64: cmp__r__p_qword rax, 0x500000bv64;
    0x400018bv64: jae__w 0x400059bv64;
ENTRY_4194334:
    0x40001ebv64: mov__r__p_qword rax, rbp - 8;
    0x400022bv64: movzx__r__p_byte ecx, rax + 0x500008bv64;
    0x40002abv64: shl__r__w ecx, 9;
    0x40002dbv64: movsxd__r__r rax, ecx;
    0x400030bv64: movabs__r__w rdx, 0x500010bv64;
    0x40003abv64: add__r__r rdx, rax;
    0x40003dbv64: mov__r__w edi, 0x500018bv64;
    0x400042bv64: mov__r__w eax, 1;
    0x400047bv64: mov__r__r rsi, rdx;
    0x40004abv64: mov__r__r rdx, rax;
    0x40004dbv64: call__w 0x500020bv64;
ENTRY_4194393:
    0x400059bv64: add__r__w rsp, 0x10bv64;
    0x40005dbv64: pop__r rbp;
    0x40005ebv64: ret;
ENTRY_5242912:

ENTRY_4194386:
    0x400052bv64: mov__p_byte__r 0x500018bv64, al;
    0x400059bv64: add__r__w rsp, 0x10bv64;
    0x40005dbv64: pop__r rbp;
    0x40005ebv64: ret;
}
