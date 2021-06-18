prog _generated_binaries_variant1_kocher_ex11_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x20bv64;
    0x400004: stp__r64__r64__t_2_r64_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400008: add__r64__r64__n gpr_29, sp, 0x10bv64;
    0x40000c: adrp__r64__n gpr_8, 0x500000bv64;
    0x400010: add__r64__r64__n gpr_8, gpr_8, 0;
    0x400014: str__r64__t_2_r64_n gpr_0, (sp, 8);
    0x400018: ldr__r64__t_2_r64_n gpr_9, (sp, 8);
    0x40001c: ldr__r64__t_1_r64 gpr_8, (gpr_8);
    0x400020: cmp__r64__r64 gpr_9, gpr_8;
    0x400024: b_hs__n 0x400074bv64;
ENTRY_4194420:
    0x400074: ldp__r64__r64__t_2_r64_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400078: add__r64__r64__n sp, sp, 0x20bv64;
    0x40007c: ret;
ENTRY_4194344:
    0x400028: ldr__r64__t_2_r64_n gpr_8, (sp, 8);
    0x40002c: adrp__r64__n gpr_9, 0x500000bv64;
    0x400030: add__r64__r64__n gpr_9, gpr_9, 8;
    0x400034: ldrb__r32__t_2_r64_r64 gpr_10, (gpr_9, gpr_8);
    0x400038: movz__r32__n gpr_11, 0x200bv64;
    0x40003c: mul__r32__r32__r32 gpr_10, gpr_10, gpr_11;
    0x400040: mov__r32__r32 gpr_0, gpr_10;
    0x400044: sxtw__r64__r32 gpr_8, gpr_0;
    0x400048: adrp__r64__n gpr_9, 0x500000bv64;
    0x40004c: add__r64__r64__n gpr_9, gpr_9, 0x10bv64;
    0x400050: add__r64__r64__r64 gpr_1, gpr_9, gpr_8;
    0x400054: adrp__r64__n gpr_8, 0x500000bv64;
    0x400058: add__r64__r64__n gpr_8, gpr_8, 0x18bv64;
    0x40005c: mov__r64__r64 gpr_0, gpr_8;
    0x400060: movz__r64__n gpr_2, 0x1bv64;
    0x400064: str__r64__t_1_r64 gpr_8, (sp);
    0x400068: bl__n 0x500020bv64;

ENTRY_4194412:
    0x40006c: ldr__r64__t_1_r64 gpr_8, (sp);
    0x400070: strb__r32__t_1_r64 gpr_0, (gpr_8);
    0x400074: ldp__r64__r64__t_2_r64_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400078: add__r64__r64__n sp, sp, 0x20bv64;
    0x40007c: ret;
}
