prog _generated_binaries_variant1_kocher_ex12_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x10bv64;
    0x400004: adrp__r64__n gpr_8, 0x500000bv64;
    0x400008: add__r64__r64__n gpr_8, gpr_8, 0;
    0x40000c: str__r64__t_2_r_n gpr_0, (sp, 8);
    0x400010: str__r64__t_1_r gpr_1, (sp);
    0x400014: ldr__r64__t_2_r_n gpr_9, (sp, 8);
    0x400018: ldr__r64__t_1_r gpr_10, (sp);
    0x40001c: add__r64__r64__r64 gpr_9, gpr_9, gpr_10;
    0x400020: ldr__r64__t_1_r gpr_8, (x8);
    0x400024: cmp__r64__r64 gpr_9, gpr_8;
    0x400028: b_hs__n 0x40006cbv64;
ENTRY_4194412:
    0x40006c: add__r64__r64__n sp, sp, 0x10bv64;
    0x400070: ret;
ENTRY_4194348:
    0x40002c: ldr__r64__t_2_r_n gpr_8, (sp, 8);
    0x400030: ldr__r64__t_1_r gpr_9, (sp);
    0x400034: add__r64__r64__r64 gpr_8, gpr_8, gpr_9;
    0x400038: adrp__r64__n gpr_9, 0x500000bv64;
    0x40003c: add__r64__r64__n gpr_9, gpr_9, 8;
    0x400040: ldrb__r32__t_2_r_r gpr_10, (x9, x8);
    0x400044: movz__r32__n gpr_11, 0x200bv64;
    0x400048: mul__r32__r32__r32 gpr_10, gpr_10, gpr_11;
    0x40004c: adrp__r64__n gpr_8, 0x500000bv64;
    0x400050: add__r64__r64__n gpr_8, gpr_8, 0x10bv64;
    0x400054: ldrb__r32__t_2_r_r_sxtw gpr_10, (x8, w10);
    0x400058: adrp__r64__n gpr_8, 0x500000bv64;
    0x40005c: add__r64__r64__n gpr_8, gpr_8, 0x18bv64;
    0x400060: ldrb__r32__t_1_r gpr_11, (x8);
    0x400064: and__r32__r32__r32 gpr_10, gpr_11, gpr_10;
    0x400068: strb__r32__t_1_r gpr_10, (x8);
    0x40006c: add__r64__r64__n sp, sp, 0x10bv64;
    0x400070: ret;
}
