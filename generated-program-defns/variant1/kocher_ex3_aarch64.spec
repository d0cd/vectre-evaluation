prog _generated_binaries_variant1_kocher_ex3_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x10bv64;
    0x400004: movz__r32__n gpr_8, 0x200bv64;
    0x400008: adrp__r64__n gpr_9, 0x400000bv64;
    0x40000c: add__r64__r64__n gpr_9, gpr_9, 1;
    0x400010: adrp__r64__n gpr_10, 0x400000bv64;
    0x400014: add__r64__r64__n gpr_10, gpr_10, 1;
    0x400018: strb__r32__t_2_r_n gpr_0, (sp, 0xfbv64);
    0x40001c: ldrb__r32__t_2_r_n gpr_11, (sp, 0xfbv64);
    0x400020: mul__r32__r32__r32 gpr_8, gpr_11, gpr_8;
    0x400024: ldrb__r32__t_2_r_r_sxtw gpr_8, (x9, w8);
    0x400028: ldrb__r32__t_1_r gpr_11, (x10);
    0x40002c: and__r32__r32__r32 gpr_8, gpr_11, gpr_8;
    0x400030: strb__r32__t_1_r gpr_8, (x10);
    0x400034: add__r64__r64__n sp, sp, 0x10bv64;
    0x400038: ret;
ENTRY_4194364:
    0x40003c: sub__r64__r64__n sp, sp, 0x20bv64;
    0x400040: stp__r64__r64__t_2_r_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x400044: add__r64__r64__n gpr_29, sp, 0x10bv64;
    0x400048: adrp__r64__n gpr_8, 0x400000bv64;
    0x40004c: add__r64__r64__n gpr_8, gpr_8, 8;
    0x400050: str__r64__t_2_r_n gpr_0, (sp, 8);
    0x400054: ldr__r64__t_2_r_n gpr_9, (sp, 8);
    0x400058: ldr__r64__t_1_r gpr_8, (x8);
    0x40005c: cmp__r64__r64 gpr_9, gpr_8;
    0x400060: b_hs__n 0x400078bv64;
ENTRY_4194424:
    0x400078: ldp__r64__r64__t_2_r_n gpr_29, gpr_30, (sp, 0x10bv64);
    0x40007c: add__r64__r64__n sp, sp, 0x20bv64;
    0x400080: ret;
ENTRY_4194404:
    0x400064: ldr__r64__t_2_r_n gpr_8, (sp, 8);
    0x400068: adrp__r64__n gpr_9, 0x400000bv64;
    0x40006c: add__r64__r64__n gpr_9, gpr_9, 1;
    0x400070: ldrb__r32__t_2_r_r gpr_0, (x9, x8);
    0x400074: bl__n 0x400000bv64;
}
