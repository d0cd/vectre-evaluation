prog _generated_binaries_variant1_kocher_ex1_aarch64 {
ENTRY_4194304:
    0x400000: sub__r64__r64__n sp, sp, 0x10bv64;
    0x400004: adrp__r64__n gpr_8, 0x400000bv64;
    0x400008: add__r64__r64__n gpr_8, gpr_8, 8;
    0x40000c: str__r64__t_2_r_n gpr_0, (sp, 8);
    0x400010: ldr__r64__t_2_r_n gpr_9, (sp, 8);
    0x400014: ldr__r64__t_1_r gpr_8, (x8);
    0x400018: cmp__r64__r64 gpr_9, gpr_8;
    0x40001c: b_hs__n 0x400058bv64;
ENTRY_4194400:
    0x400060: ret;
ENTRY_4194392:
    0x400058: add__r64__r64__n sp, sp, 0x10bv64;
    0x40005c: ret;
ENTRY_4194336:
    0x400020: ldr__r64__t_2_r_n gpr_8, (sp, 8);
    0x400024: adrp__r64__n gpr_9, 0x400000bv64;
    0x400028: add__r64__r64__n gpr_9, gpr_9, 1;
    0x40002c: ldrb__r32__t_2_r_r gpr_10, (x9, x8);
    0x400030: movz__r32__n gpr_11, 0x200bv64;
    0x400034: mul__r32__r32__r32 gpr_10, gpr_10, gpr_11;
    0x400038: adrp__r64__n gpr_8, 0x400000bv64;
    0x40003c: add__r64__r64__n gpr_8, gpr_8, 1;
    0x400040: ldrb__r32__t_2_r_r_sxtw gpr_10, (x8, w10);
    0x400044: adrp__r64__n gpr_8, 0x400000bv64;
    0x400048: add__r64__r64__n gpr_8, gpr_8, 1;
    0x40004c: ldrb__r32__t_1_r gpr_11, (x8);
    0x400050: and__r32__r32__r32 gpr_10, gpr_11, gpr_10;
    0x400054: strb__r32__t_1_r gpr_10, (x8);
    0x400058: add__r64__r64__n sp, sp, 0x10bv64;
    0x40005c: ret;
}
